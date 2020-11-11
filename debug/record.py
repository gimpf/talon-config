# based upon example from aegis via #beta channel on slack, https://talonvoice.slack.com/files/U7FHVS4B0/F0142MU43GB/record.py
import os
import shutil
import struct
import wave
import time

from talon import Context, Module, actions, speech_system
from talon.lib import flac
from talon_init import TALON_HOME

OUTPUT_BASE_DIR = TALON_HOME / "../Audio/recordings"

output_dir_initialized = False
recording_dir = None
bad_recording_dir = None
current_phrase = None


def ensure_output_dir_initialized():
    global recording_dir
    global bad_recording_dir
    global output_dir_initialized

    if output_dir_initialized:
        return

    session = 0
    recording_dir = OUTPUT_BASE_DIR / "session-000"
    while recording_dir.exists():
        session += 1
        recording_dir = OUTPUT_BASE_DIR / f"session-{session:03d}"

    bad_recording_dir = recording_dir / "bad"

    os.makedirs(recording_dir, exist_ok=True)
    os.makedirs(bad_recording_dir, exist_ok=True)

    output_dir_initialized = True


mod = Module()

always_record = mod.setting(
    "recorder_record_all",
    type=int,
    default=0,
    desc="record all phrases automatically after recognition",
)

# in case we want to use an explicit action to record something, we need to have that
# set-up before the action starts running
def pre_phrase(d):
    global current_phrase
    current_phrase = d


def post_phrase(d):
    if always_record.get():
        phrase = " ".join(getattr(d["parsed"], "_unmapped", d["phrase"]))
        actions.self.record_audio(phrase)


speech_system.register("pre:phrase", pre_phrase)
speech_system.register("post:phrase", post_phrase)

phrase = 0
path_history = []
path_history_len = 2


def write_flac(path, samples):
    flac.write_flac(str(path), samples, compression_level=5)


def write_wav(path, samples):
    scaled = (min(32767, max(-32768, int(s * 32768))) for s in samples)
    binary = struct.pack("<{}h".format(len(samples)), *scaled)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(16000)
        w.writeframes(binary)


@mod.action
def record_audio(words: str):
    """Record the phrase audio to a file"""
    t = time.time()
    global phrase, path_history, path_history_len
    words = words.strip()
    if not current_phrase or not current_phrase.get("samples") or not words:
        return

    samples = current_phrase["samples"]
    filetype = ".flac"
    ensure_output_dir_initialized()
    path = recording_dir / f"{phrase:04d} {words}{filetype}"
    phrase += 1

    n = 0
    while path.exists():
        n += 1
        path = recording_dir / f"{phrase:04d} {words}-{n}{filetype}"

    if filetype == ".flac":
        write_flac(path, samples)
    elif filetype == ".wav":
        write_wav(path, samples)

    elapsed = time.time() - t
    print(f"saved in {elapsed * 1000:.2f}ms: {path}")
    path_history.append(path)
    path_history = path_history[-path_history_len:]


@mod.action
def replay_wav(path: str):
    """Replay a wave file into the speech engine"""
    ensure_output_dir_initialized()
    if not os.path.isabs(path) and not os.sep in path:
        path = recording_dir / path
    with wave.open(str(path), "rb") as w:
        frames = w.readframes(w.getnframes())
    samples = struct.unpack("<{}h".format(len(frames) // 2), frames)
    speech_system.engine.engine._on_audio_frame(samples, pad=False)


@mod.action
def mark_last_recording_as_bad():
    """Move last recorded audio file to bad folder"""
    ensure_output_dir_initialized()
    # TODO support marking older history items
    if len(path_history) >= 1:
        shutil.move(str(path_history[-1]), str(bad_recording_dir))
        print(f"marked path '{path_history[-1]}' as bad")


@mod.action
def delete_last_recording():
    """Deletes the last recorded file"""
    if len(path_history) == 0:
        return

    # TODO support marking older history items
    os.remove(str(path_history[-1]))
    print(f"deleted path '{path_history[-1]}'")
