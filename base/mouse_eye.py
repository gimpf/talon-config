from talon import ctrl, Module, Context, actions
from talon_plugins import eye_mouse, eye_zoom_mouse
from talon_plugins.eye_mouse import config as gaze_config, toggle_camera_overlay, toggle_control

mod = Module()

@mod.action_class
class Actions:
    def gaze_calibrate():
        """Calibrate eye tracker"""
        eye_mouse.calib_start()

    def gaze_toggle_cam():
        """Show camera overlay from eye tracker"""
        toggle_camera_overlay(not gaze_config.show_camera)

    def gaze_toggle_control():
        """Toggles controlling mouse via gaze"""
        toggle_control(not gaze_config.control_mouse)

    def gaze_enable_zoom():
        """Activates controlling mouse via gaze with zoom"""
        eye_zoom_mouse.toggle_zoom_mouse(True)

    def gaze_disable_zoom():
        """Disables zoom mode for controlling mouse via gaze"""
        eye_zoom_mouse.toggle_zoom_mouse(False)

    def gaze_cancel_zoom():
        """Cancel zoom mouse if pending"""
        if eye_zoom_mouse.zoom_mouse.enabled and eye_zoom_mouse.zoom_mouse.state != eye_zoom_mouse.STATE_IDLE:
            eye_zoom_mouse.zoom_mouse.cancel()
