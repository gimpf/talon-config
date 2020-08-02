mode: dictation
mode: command
-
^talon sleep$:
    mode.save()
    speech.disable()
    user.disable_minor_mode('coma')

^talon coma$:
    mode.save()
    speech.disable()
    mode.disable('noise')
    mode.disable('hotkey')
    # the following is a workaround while 'noise' mode isn't finished yet
    user.enable_minor_mode('coma')
