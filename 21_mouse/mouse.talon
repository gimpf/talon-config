mode: command
-
# from knausj_talon, misc/mouse.py
settings():
    user.mouse_scroll_sensitivity = 1

^talon enable eye mouse control$:
    user.eye_mouse_wake()

^talon deactivate eye mouse control$:
    user.mouse_sleep()

^talon calibrate eye mouse$:
    user.mouse_calibrate()

^talon enable eye mouse zoom$:
    user.eye_mouse_enable_zoom_mouse()

^talon deactivate eye mouse zoom$:
    user.eye_mouse_disable_zoom_mouse()

^talon cancel eye mouse zoom$:
    user.eye_mouse_cancel_zoom_mouse()

^talon toggle camera overlay$:
    eye_mouse.camera_overlay.toggle()

^talon stop mouse [control]$:
    user.mouse_sleep()

^talon show mouse cursor$: user.mouse_show_cursor()
^talon hide mouse cursor$: user.mouse_hide_cursor()

mouse click:
    mouse_click()

mouse click <user.mouse_clickspec>:
    user.mouse_click(mouse_clickspec)

mouse chord <user.modifiers> <user.mouse_index>:
    key("{modifiers}:down")
    mouse_click(mouse_index)
    key("{modifiers}:up")

mouse double click:
    mouse_click()
    mouse_click()

mouse triple click:
    mouse_click()
    mouse_click()
    mouse_click()

mouse drag:    user.mouse_drag()

mouse center:
    user.mouse_center()

mouse position <user.mouse_position>:
    user.mouse_set_position(mouse_position)

mouse move <user.directions>:
    user.mouse_move(directions)

mouse wheel down: user.mouse_scroll_down()
mouse wheel start down: user.mouse_start_scrolling_down()
mouse wheel up: user.mouse_scroll_up()
mouse wheel start up: user.mouse_start_scrolling_up()
mouse gaze wheel: user.mouse_scroll_by_cursor()
mouse wheel stop: user.mouse_stop_scrolling()
