from talon import cron, ctrl, ui, Module, Context, actions
from talon_plugins import eye_mouse, eye_zoom_mouse
from time import sleep

mod = Module()
mod.setting("mouse_scroll_sensitivity", type=int, default=1, desc="Speed of scrolling")
mod.list("mouse_button", desc="maps names of mouse buttons to their numerical index")

@mod.capture(rule="{self.mouse_button}")
def mouse_index(m) -> int:
    "One mouse button index"
    return int(m.mouse_button)

@mod.capture(rule="[({self.mouse_button} | <user.numeral_adverb> | {self.mouse_button} <user.numeral_adverb>)]")
def mouse_clickspec(m) -> (int, int):
    "Captures which mouse button is to be pressed for how many times."
    btn = 0
    times = 1
    if hasattr(m, "mouse_button"):
        btn = int(m.mouse_button)
    if hasattr(m, "numeral_adverb"):
        times = m.numeral_adverb
    return (btn, times)

@mod.capture(rule='{self.direction} <number>')
def direction(m) -> str:
    "Captures a relative movement in a specific direction"
    speed = [0.0, 0.0]
    if m.direction == 'up':
        speed = [0.0, -1.0]
    elif m.direction == 'right':
        speed = [1.0, 0.0]
    elif m.direction == 'down':
        speed = [0.0, 1.0]
    elif m.direction == 'left':
        speed = [-1.0, 0.0]
    res = [x * m.number_signed for x in speed]
    res = f'{int(res[0])},{int(res[1])}'
    print(f'direction: {res}')
    return res


@mod.capture(rule='<user.direction>+')
def directions(m) -> str:
    "Captures directions consisting of several relative movements"
    res = ' '.join(m.direction_list)
    print(f'directions: {res}')
    return res


@mod.action_class
class Actions:
    def mouse_center():
        """Centers the mouse cursor in the primary screen."""
        rect = ui.screen.main_screen().rect
        x = rect.x + rect.width / 2
        y = rect.y + rect.height / 2
        ctrl.mouse_move(x, y)

    def mouse_move(directions: str):
        """Moves the mouse relative to the current position"""
        for d in directions.split(" "):
            [dx, dy] = d.split(",")
            dx, dy = int(dx), int(dy)
            x, y = ctrl.mouse_pos()
            print(f'current mouse pos: {x},{y}, move {dx},{dy}')
            ctrl.mouse_move(x+dx, y+dy)

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
