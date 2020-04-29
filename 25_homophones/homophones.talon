# taken from https://github.com/knausj85/knausj_talon/blob/master/text/homophones.talon
mode: command
-
homophones help: user.homophones_show_help()
show homophones:
    edit.copy()
    sleep(100ms)
    user.homophones_show_for_selection(user.get_clip())

homophones <user.homophones_canonical>: user.homophones_show(homophones_canonical)

pick homophone <user.homophones_selection>:
    insert(homophones_selection)
    user.homophones_hide()

hide homophones: user.homophones_hide()

format <user.formatters> homophones <user.homophones_selection>:
    insert(user.formatters_format_text(homophones_selection, formatters))
    user.homophones_hide()
