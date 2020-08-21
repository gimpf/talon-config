from talon import cron, ctrl, ui, Module, Context, actions
from talon.engine import engine
from talon_plugins import speech, eye_mouse, eye_zoom_mouse
from time import sleep

mod = Module()
mod.setting("mouse_scroll_sensitivity", type=int, default=1, desc="Speed of scrolling")
mod.list("mouse_button", desc="maps names of mouse buttons to their numerical index")

@mod.capture
def mouse_index(m) -> int:
    "One mouse button index"


@mod.capture
def mouse_clickspec(m) -> (int, int):
    "Captures which mouse button is to be pressed for how many times."


@mod.action_class
class Actions:
    def mouse_center():
        """Centers the mouse cursor in the primary screen."""
        rect = ui.screen.main_screen().rect
        x = rect.x + rect.width / 2
        y = rect.y + rect.height / 2
        ctrl.mouse_move(x, y)

    def mouse_click(clickspec: (int, int)):
        """Clicks a mouse button as many times, as specified in clickspec"""
        btn, times = clickspec
        for _ in range(times):
            actions.mouse_click(button=btn)

    def mouse_scroll_down():
        """Scrolls down"""
        actions.mouse_scroll(
            by_lines=False, y=int(ctx.settings["user.mouse_scroll_sensitivity"])
        )

    def mouse_scroll_up():
        """Scrolls up"""
        actions.mouse_scroll(
            by_lines=False, y=-int(ctx.settings["user.mouse_scroll_sensitivity"])
        )


ctx = Context()
ctx.settings["self.mouse_scroll_sensitivity"] = 5
ctx.lists["self.mouse_button"] = {
    "left": "0",
    "right": "1",
    "middle": "2",
}


@ctx.capture(rule="{self.mouse_button}")
def mouse_index(m) -> int:
    return int(m.mouse_button)


@ctx.capture(
    rule="[({self.mouse_button} | <user.numeral_adverb> | {self.mouse_button} <user.numeral_adverb>)]"
)
def mouse_clickspec(m) -> (int, int):
    btn = 0
    times = 1
    if hasattr(m, "mouse_button"):
        btn = int(m.mouse_button)
    if hasattr(m, "numeral_adverb"):
        times = m.numeral_adverb
    return (btn, times)
