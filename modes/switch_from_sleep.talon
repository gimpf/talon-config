mode: sleep
-
^talon wake up gently$:
    speech.enable()
    mode.restore()
    # the following is a workaround while 'noise' mode isn't finished yet
    user.disable_minor_mode('coma')
    # notifications are off in sleep, and so the wake-up command would not be shown; workaround
    app.notify("talon has been activated")

^talon coma$:
    # the following is a workaround while 'noise' mode isn't finished yet
    user.enable_minor_mode('coma')
    app.notify("talon is in a coma")
