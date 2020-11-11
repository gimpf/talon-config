mode: command
-
^talon dictation mode$:
    mode.disable("command")
    mode.enable("dictation")

^talon direct command$:
    # non-prefixed spelling only works well enough with headset mic
    user.enable_minor_mode('direct')
    app.notify("talon is in direct command mode")

^talon prefixed command$:
    user.disable_minor_mode('direct')
    app.notify("talon is in prefixed command mode")
