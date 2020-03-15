from talon import noise, actions, ctrl


def on_pop(active):
    # for pop active = False always
    actions.mouse_click(button=1)


def on_hiss(active):
    ctrl.mouse_click(button=0, down=active, up=not active)


noise.register('pop', on_pop)
noise.register('hiss', on_hiss)
