mode: command
-
format <user.formatters> [phrase] <user.phrase>$: insert(user.formatters_format_text(phrase, formatters))
set format <user.formatters>: user.formatters_set(formatters)
formatted <user.phrase>$: insert(user.formatters_formatted(phrase))
