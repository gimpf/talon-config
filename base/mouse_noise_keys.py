from talon import noise, ctrl, settings
from talon_plugins import eye_mouse, eye_zoom_mouse


def on_pop(active):
    if not settings.get("user.noise_enabled"):
        return
    # # for pop active = False always
    if not eye_zoom_mouse.zoom_mouse.enabled:
        ctrl.mouse_click(button=1)
        # ctrl.mouse_click(button=0, hold=16000)
        # if setting_mouse_enable_pop_click.get() >= 1:

def on_hiss(active):
    if not settings.get("user.noise_enabled"):
        return
    if not eye_zoom_mouse.zoom_mouse.enabled or eye_zoom_mouse.zoom_mouse.state == eye_zoom_mouse.STATE_IDLE:
        ctrl.mouse_click(button=0, down=active, up=not active)


noise.register("pop", on_pop)
noise.register("hiss", on_hiss)
