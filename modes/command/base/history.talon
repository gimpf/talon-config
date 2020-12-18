mode: command
-
# settings():
#    user.history_show_notifications = 1

^show command history$:
    user.history_show()

^hide command history$:
    user.history_hide()

^clear command history$:
    user.history_clear()
