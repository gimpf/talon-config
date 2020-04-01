mode: sleep
-
^talon wake up gently$:
    speech.enable()
    # should be similar to
    # mode.disable('sleep')
    # mode.restore('dictation command')

<word>+: user.ignore(word_list)
