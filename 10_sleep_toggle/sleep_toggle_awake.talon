mode: dictation
mode: command
-
settings():
    user.noise_enabled = 'True'

^talon sleep$:
    mode.save()
    speech.disable()

^talon fall into a coma$:
    mode.save()
    speech.disable()
    mode.disable('noise')
    mode.disable('hotkey')
    # the following is a workaround while 'noise' mode isn't finished yet
    mode.enable('user.coma')
