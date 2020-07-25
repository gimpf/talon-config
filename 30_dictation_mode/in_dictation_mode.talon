mode: dictation
-
# a rather minimal dictation mode, based upon an example by aegis in the beta channel
^switch to command mode$:
    mode.disable("dictation")
    mode.enable("command")

# use this to dictate phrases that are would otherwise be commands
^escape <phrase>$:
    dictate.natural(phrase)
    insert(" ")

<phrase>:
    dictate.natural(phrase)
    insert(" ")

capitalize <phrase>:
    insert(user.formatters_format_text(phrase, "sentence"))
    insert(" ")

enter: key(enter)
period: key(backspace . space)
comma: key(backspace , space)
colon: key(backspace : space)
semicolon: key(backspace ; space)
question mark: key(backspace ? space)
exclamation mark: key(backspace ! space)
