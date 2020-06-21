mode: command
-
^print all actions$:
    user.print_all_actions()

^print all captures$:
    user.print_all_captures()

^print out application$:
    name = app.name()
    exe = app.executable()
    print("active application:")
    print("    app.name: {name}")
    print("    app.executable: {exe}")

^print out last phrases$:
    user.print_last_phrases()
