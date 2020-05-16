mode: sleep
-
settings():
    user.noise_enabled = 'True'

^talon wake up gently$:
    speech.enable()
    mode.restore()
    # the following is a workaround while 'noise' mode isn't finished yet
    mode.disable('user.coma')

<word>+:
    skip()
