mode: command
-
settings():
    user.recorder_record_all = 0

^print all actions$:
    user.print_all_actions()

^print all captures$:
    user.print_all_captures()

^print current application$:
    name = app.name()
    executable =  app.executable()
    bundle = app.bundle()
    title = win.title()
    print("Active Application:")
    print("    Name: {name}")
    print("    Executable: {executable}")
    print("    Bundle: {bundle}")
    print("    Title: {title}")

^print last phrases$:
    user.print_last_phrases()
