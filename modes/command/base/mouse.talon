mode: command
-
click <user.mouse_clickspec>:
    user.mouse_click(mouse_clickspec)

tickle:
    user.mouse_move("1,0 -1,0 0,1 0,-1")

mouse center:
    user.mouse_center()

wheel down: user.mouse_scroll_down()
wheel up: user.mouse_scroll_up()
