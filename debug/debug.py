# from talon examples https://github.com/talonvoice/examples/blob/master/debug.py
from talon import noise, actions, ctrl, speech_system
from talon.microphone import manager

debugEngine = True
debugNoise = True
debugMic = True


def listener(topic, m):
    if topic == "cmd" and m["cmd"]["cmd"] == "g.load" and m["success"] == True:
        print("speech_system event: [grammar reloaded]")
    else:
        print(f"speech_system event: {topic}", m)


if debugEngine:
    speech_system.register("", listener)


def on_mic_ev(topic, arg):
    print(f"mic event: {topic} {arg}")


if debugMic:
    manager.register("", on_mic_ev)

# def on_pop(active):
#     print(f"pop active:{active}")
#
# def on_hiss(active):
#     print(f"hiss active:{active}")
#
# noise.register('pop', on_pop)
# noise.register('hiss', on_hiss)


def on_noise(noise, active):
    print(f"noise {noise} active:{active}")


if debugNoise:
    noise.register("", on_noise)
