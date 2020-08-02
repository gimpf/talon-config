mode: dictation
-
# a rather minimal dictation mode, based upon an example by aegis in the beta channel
# use this to dictate phrases that are would otherwise be commands
^escape <user.phrase>$:
    # dictate.natural or auto_insert for proper capitalization?
    insert(phrase)
    insert(" ")

<user.phrase>:
    # dictate.natural or auto_insert for proper capitalization?
    insert(phrase)
    insert(" ")

capitalize <user.phrase>:
    insert(user.formatters_format_text(phrase, "sentence"))
    insert(" ")

enter: key(enter)
period: key(backspace . space)
comma: key(backspace , space)
colon: key(backspace : space)
semicolon: key(backspace ; space)
question mark: key(backspace ? space)
exclamation mark: key(backspace ! space)
