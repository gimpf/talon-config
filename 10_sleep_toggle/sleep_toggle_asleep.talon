mode: sleep
-
settings():
    user.noise_enabled = 'True'

^talon wake up gently$:
    speech.enable()
    mode.restore()
    # should be similar to
    # mode.disable('sleep')
    # mode.restore('dictation, command, noise, hotkey')
    # the following is a workaround while 'noise' mode isn't finished yet
    mode.disable('user.coma')

<word>+: user.ignore(word_list)
