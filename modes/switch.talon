mode: dictation
mode: command
-
^talon sleep$:
    mode.save()
    speech.disable()
    user.disable_minor_mode('coma')
    app.notify("talon is asleep now")

^talon coma$:
    mode.save()
    speech.disable()
    mode.disable('noise')
    mode.disable('hotkey')
    # the following is a workaround while 'noise' mode isn't finished yet
    user.enable_minor_mode('coma')
    app.notify("talon is in a coma")
