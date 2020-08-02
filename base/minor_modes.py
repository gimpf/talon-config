from talon import Module

# TODO remove once AND queries in modes work
mod = Module()

current_minor_modes = set({})
current_minor_modes_enc = ""

# define the minor-mode scope
#
# Why using a separate scope instead of just mode itself?
#
# 'and' queries for match sections still have some limitations,
# a query like 'mode = command AND mode = noise' is currently
# not supported (you can make the match section parse, but the
# match will never activate - as of v1425).
#
# This will likely change sooner or later, in the meantime,
# use minor modes to make ends meet.
#
# To support multiple minor modes at the same time, these
# are encoded as a string, sorted by name, to be matched via
# regex.
@mod.scope
def scope():
    return {"minor-mode": current_minor_modes_enc}


@mod.action_class
class Actions:
    def enable_minor_mode(mode: str):
        """enable the specified minor mode"""
        global current_minor_modes_enc
        if mode in current_minor_modes:
            return
        current_minor_modes.add(mode)
        current_minor_modes_enc = " ".join(sorted(current_minor_modes))
        print(f"enabled minor mode {mode} - now: {current_minor_modes_enc}")
        scope.update()

    def disable_minor_mode(mode: str):
        """disable the specified minor mode"""
        global current_minor_modes_enc
        if not mode in current_minor_modes:
            return
        current_minor_modes.remove(mode)
        current_minor_modes_enc = " ".join(sorted(current_minor_modes))
        print(f"disabled minor mode {mode} - now: {current_minor_modes_enc}")
        scope.update()

    def clear_minor_modes():
        """disable all minor modes"""
        global current_minor_modes_enc
        if not bool(current_minor_modes):
            return
        current_minor_modes.clear()
        current_minor_modes_enc = ""
        print(f"cleared minor modes - now: {current_minor_modes_enc}")
        scope.update()
