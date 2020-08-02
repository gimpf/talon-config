from talon import noise, ctrl, settings


def on_pop(active):
    # for pop active = False always
    if settings.get("user.noise_enabled"):
        ctrl.mouse_click(button=1)


def on_hiss(active):
    if settings.get("user.noise_enabled"):
        ctrl.mouse_click(button=0, down=active, up=not active)


noise.register("pop", on_pop)
noise.register("hiss", on_hiss)
