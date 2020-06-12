from talon import Module

mod = Module()

current_minor_modes = set({})

# define the minor-mode scope
# Why using a separate scope instead of just mode itself?
# Because for know, "and" queries on modes (like "command mode AND talon-minor mode")
# is not sensibly supported for talon file matches
# This is not unlikely to change sooner or later.
# In the meantime, use a separate scope.
@mod.scope
def scope():
    return {'minor-mode': current_minor_modes}


# Very minimal set of commands.
# Supporting a help for showing all minor modes, and all active minor-modes,
# would be a welcome addition.
@mod.action_class
class Actions:
    def enable_minor_mode(mode: str):
        """enable the specified minor mode"""
        global current_minor_modes
        current_minor_modes.add(mode)
        scope.update()

    def disable_minor_mode(mode: str):
        """disable the specified minor mode"""
        global current_minor_modes
        if mode in current_minor_modes:
            current_minor_modes.remove(mode)
        scope.update()

    def clear_minor_modes():
        """disable all minor modes"""
        global current_minor_modes
        current_minor_modes.clear()
        scope.update()
