from talon import Context, speech_system, actions
from talon_plugins import speech

# prior art: knausj_talon/code/sleep_toggle.py


def ignore(m):
    print(f'ignored phrase: {m}')


ctx_asleep = Context()
ctx_awake = Context()


def set_enabled(value):
    ctx_asleep.exclusive = not value
    ctx_asleep.enabled = not value
    actions.speech.toggle(value)


ctx_asleep.commands = {
    '^talon wake up gently$': lambda m: set_enabled(True),
    # this reduces the risk that Talon incorrectly interprets arbitrary words as the wakeup a command
    '<word>+': ignore,
}

ctx_awake.commands = {
    '^talon sleep$': lambda m: set_enabled(False),
}

# during startup action.speech.toggle is not yet available, but seemingly also not necessary
ctx_asleep.exclusive = False
ctx_asleep.enabled = False
