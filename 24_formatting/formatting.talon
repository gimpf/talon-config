mode: command
-
format <user.formatters> phrase <phrase>$: insert(user.formatters_format_text(phrase, formatters))
format <user.formatters> (word | words) <word>+$: insert(user.formatters_format_text(word_list, formatters))
