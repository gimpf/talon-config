mode: dictation
mode: command
-
^talon sleep$:
    speech.disable()
    # should be similar to
    # mode.save('dictation command')
    # mode.disable('dictation')
    # mode.disable('command')
    # mode.enable('sleep')
