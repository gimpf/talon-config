mode: sleep
-
^talon wake up gently$:
    speech.enable()
    mode.restore()
    # should be similar to
    # mode.disable('sleep')
    # mode.restore('dictation, command, noise, hotkey')

<word>+: user.ignore(word_list)
