mode: command
-
settings():
    user.recorder_record_all = 1

^print all actions$:
    user.print_all_actions()

^print all captures$:
    user.print_all_captures()

^print current application$:
    name = app.name()
    exe = app.executable()
    print("active application:")
    print("    app.name: {name}")
    print("    app.executable: {exe}")

^print last phrases$:
    user.print_last_phrases()
