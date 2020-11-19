mode: command
mode: dictation
-
^gaze calibrate$:
    user.gaze_calibrate()

^gaze camera$:
    user.gaze_toggle_cam()

^gaze control$:
    user.gaze_toggle_control()

^gaze zoom enable$:
    user.gaze_enable_zoom()

^gaze zoom off$:
    user.gaze_disable_zoom()

^gaze zoom cancel$:
    user.gaze_cancel_zoom()
