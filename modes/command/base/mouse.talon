mode: command
-
click:
    user.mouse_click()

click <user.mouse_clickspec>:
    user.mouse_click(mouse_clickspec)

tickle:
    user.mouse_move("1,0 -1,0 0,1 0,-1")

mouse center:
    user.mouse_center()

mouse <number> left:
    x = mouse_x()
    x = x - number
    y = mouse_y()
    mouse_move(x, y)

mouse <number> right:
    x = mouse_x()
    x = x + number
    y = mouse_y()
    mouse_move(x, y)

mouse <number> down:
    x = mouse_x()
    y = mouse_y()
    y = y + number
    mouse_move(x, y)

mouse <number> up:
    x = mouse_x()
    y = mouse_y()
    y = y - number
    mouse_move(x, y)

wheel down: user.mouse_scroll_down()
wheel up: user.mouse_scroll_up()
