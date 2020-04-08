mode: dictation
mode: command
-
settings():
    user.noise_enabled = 'True'

^talon sleep$:
    mode.save()
    speech.disable()
    # should be similar to
    # mode.save('dictation, command')
    # mode.disable('dictation')
    # mode.disable('command')
    # mode.enable('sleep')

^talon fall into a coma$:
    mode.save()
    speech.disable()
    mode.disable('noise')
    mode.disable('hotkey')
    # should be similar to
    # mode.save('dictation, command, noise, hotkey')
    # mode.disable('dictation')
    # mode.disable('command')
    # mode.disable('noise')
    # mode.disable('hotkey')
    # mode.enable('sleep')
    # the following is a workaround while 'noise' mode isn't finished yet
    mode.enable('user.coma')
