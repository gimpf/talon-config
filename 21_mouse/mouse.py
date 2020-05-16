# from knausj_talon, code/mouse.py
from talon import cron, ctrl, ui, Module, Context, actions
from talon.engine import engine
from talon_plugins import speech, eye_mouse, eye_zoom_mouse
from time import sleep

dragging = False
active_job = None


def stop_scrolling():
    global active_job
    if active_job:
        cron.cancel(active_job)
    active_job = None


def start_scrolling(interval: str, speed: int):
    global active_job
    stop_scrolling()
    active_job = cron.interval(
        interval, lambda: actions.mouse_scroll(by_lines=False, y=speed))


def scroll_by_cursor():
    windows = ui.windows()
    window = None
    x, y = ctrl.mouse_pos()
    for w in windows:
        if w.rect.contains(x, y):
            window = w.rect
            break
    if window is None:
        return

    midpoint = window.y + window.height / 2
    amount = int(((y - midpoint) / (window.height / 10)) ** 3)
    actions.mouse_scroll(by_lines=False, y=amount)


def start_cursor_scrolling():
    global active_job
    stop_scrolling()
    active_job = cron.interval("60ms", scroll_by_cursor)


mod = Module()
mod.setting('mouse_scroll_sensitivity', type='int', desc='Speed of scrolling')
mod.list('corner', desc='names for corners of a rectangle')
mod.list('edge', desc='names for edges of a rectangle')
mod.list('area', desc='names for subtiles of a 3x3 divided rectangle')
mod.list('direction', desc='names for going somewhere on a screen')


@mod.capture
def mouse_index(m) -> int:
    "One mouse button index"


@mod.capture
def mouse_clickspec(m) -> (int, int):
    "Captures which mouse button is to be pressed for how many times."


@mod.capture
def mouse_position(m) -> (int, int):
    "Screen-relative target position for a mouse action."


@mod.capture
def direction(m) -> str:
    "Relative movement in x,y, returned as string with comma separated dx,dy"


@mod.capture
def directions(m) -> str:
    "Multiple steps of relative movement in x,y returned as a space separated list of comma separated dx,dy steps"


@mod.action_class
class Actions:
    def eye_mouse_wake():
        """Enable control mouse, zoom mouse, and disables cursor"""
        eye_zoom_mouse.zoom_mouse.enable()
        eye_mouse.control_mouse.enable()
        ctrl.cursor_visible(False)

    def eye_mouse_calibrate():
        """Start calibration"""
        eye_mouse.calib_start()

    def eye_mouse_enable_zoom_mouse():
        """Enables zoom mouse"""
        eye_zoom_mouse.zoom_mouse.enable()

    def eye_mouse_disable_zoom_mouse():
        """Disables zoom mouse"""
        eye_zoom_mouse.zoom_mouse.disable()

    def eye_mouse_cancel_zoom_mouse():
        """Cancel zoom mouse if pending"""
        if eye_zoom_mouse.zoom_mouse.enabled and eye_zoom_mouse.zoom_mouse.state != eye_zoom_mouse.STATE_IDLE:
            eye_zoom_mouse.zoom_mouse.cancel()

    def mouse_show_cursor():
        """Shows the cursor"""
        ctrl.cursor_visible(True)

    def mouse_hide_cursor():
        """Hides the cursor"""
        ctrl.cursor_visible(False)

    def mouse_center():
        """Centers the mouse cursor in the primary screen."""
        rect = ui.screen.main_screen().rect
        x = rect.x + rect.width / 2
        y = rect.y + rect.height / 2
        ctrl.mouse_move(x, y)

    def mouse_set_position(coordinates: (int, int)):
        """Set mouse position to specified coordinates"""
        x, y = coordinates
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

    def mouse_drag():
        """(TEMPORARY) Press and hold/release button 0 depending on state for dragging"""
        global dragging
        if not dragging:
            dragging = True
            ctrl.mouse_click(button=0, down=True)
        else:
            dragging = False
            ctrl.mouse_click(up=True)

    def mouse_sleep():
        """Disables control mouse, zoom mouse, and re-enables cursor"""
        global dragging
        eye_zoom_mouse.zoom_mouse.disable()
        eye_mouse.control_mouse.disable()
        ctrl.cursor_visible(True)
        stop_scrolling()
        if dragging:
            mouse_drag()

    def mouse_scroll_down():
        """Scrolls down"""
        stop_scrolling()
        actions.mouse_scroll(by_lines=False, y=int(
            5*ctx.settings['user.mouse_scroll_sensitivity']))

    def mouse_start_scrolling_down():
        """Scrolls down continuously"""
        stop_scrolling()
        start_scrolling("200ms", min(
            1, ctx.settings['user.mouse_scroll_sensitivity']))

    def mouse_scroll_up():
        """Scrolls up"""
        stop_scrolling()
        actions.mouse_scroll(by_lines=False, y=-
                             ctx.settings['user.mouse_scroll_sensitivity'])

    def mouse_start_scrolling_up():
        """Scrolls up continuously"""
        stop_scrolling()
        start_scrolling(
            "200ms", -ctx.settings['user.mouse_scroll_sensitivity'])

    def mouse_stop_scrolling():
        """Stops scrolling"""
        stop_scrolling()

    def mouse_scroll_by_cursor():
        """Starts gaze scroll"""
        start_cursor_scrolling()


ctx = Context()
ctx.settings['self.mouse_scroll_sensitivity'] = 1
ctx.lists['self.mouse_button'] = {
    'left':    '0',
    'right':   '1',
    'middle':  '2',
}
ctx.lists['self.direction'] = ['up', 'right', 'down', 'left']
ctx.lists['self.corner'] = ['upper left',
                            'upper right', 'lower left', 'lower right']
ctx.lists['self.edge'] = ['top',  'right', 'bottom', 'left']
ctx.lists['self.area'] = [
    'upper left', 'upper center', 'upper right',
    'mid left',   'center',       'mid right',
    'lower left', 'lower center', 'lower right']


@ctx.capture(rule='{self.mouse_button}')
def mouse_index(m) -> int:
    return int(m.mouse_button)

# for a strange reason this doesn't work: @ctx.capture(rule='([{self.mouse_button}] [<user.numeral_adverb>])')
@ctx.capture(rule='({self.mouse_button} | <user.numeral_adverb> | {self.mouse_button} <user.numeral_adverb>)')
def mouse_clickspec(m) -> (int, int):
    btn = 0
    times = 1
    if hasattr(m, 'mouse_button'):
        btn = int(m.mouse_button)
    if hasattr(m, 'numeral_adverb'):
        times = m.numeral_adverb
    return (btn, times)


@ctx.capture(rule='{self.direction} <number_signed>')
def direction(m) -> str:
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


@ctx.capture(rule='<user.direction>+')
def directions(m) -> str:
    res = ' '.join(m.direction_list)
    print(f'directions: {res}')
    return res


@ctx.capture(rule='{self.corner} corner | {self.edge} edge | {self.edge} bar | {self.area} area')
def mouse_position(m) -> (int, int):
    typ = m[-1]
    scr = ui.active_window().screen.rect
    res = (0, 0)
    if typ == 'corner':
        pos = m.corner
        if pos == 'upper left':
            res = (scr.x, scr.y)
        elif pos == 'upper right':
            res = (scr.x + scr.width, scr.y)
        elif pos == 'lower left':
            res = (scr.x, scr.y + scr.height)
        elif pos == 'lower right':
            res = (scr.x + scr.width, scr.y + scr.height)
    elif typ == 'edge':
        pos = m.edge
        if pos == "top":
            res = (scr.x + scr.width/2, scr.y)
        elif pos == "right":
            res = (scr.x + scr.width,   scr.y + scr.height/2)
        elif pos == "bottom":
            res = (scr.x + scr.width/2, scr.y + scr.height)
        elif pos == "left":
            res = (scr.x,               scr.y + scr.height/2)
    elif typ == 'bar':
        pos = m.edge
        BAR_MID = 10
        if pos == "top":
            res = (scr.x + scr.width/2,         scr.y + BAR_MID)
        elif pos == "right":
            res = (scr.x + scr.width - BAR_MID, scr.y + scr.height/2)
        elif pos == "bottom":
            res = (scr.x + scr.width/2,         scr.y + scr.height - BAR_MID)
        elif pos == "left":
            res = (scr.x + BAR_MID,             scr.y + scr.height/2)
    elif typ == 'area':
        pos = m.area
        if pos == 'upper left':
            res = (scr.x + scr.width * 1/4, scr.y + scr.height * 1/4)
        elif pos == 'upper center':
            res = (scr.x + scr.width * 2/4, scr.y + scr.height * 1/4)
        elif pos == 'upper right':
            res = (scr.x + scr.width * 3/4, scr.y + scr.height * 1/4)
        elif pos == 'mid left':
            res = (scr.x + scr.width * 1/4, scr.y + scr.height * 2/4)
        elif pos == 'center':
            res = (scr.x + scr.width * 2/4, scr.y + scr.height * 2/4)
        elif pos == 'mid right':
            res = (scr.x + scr.width * 3/4, scr.y + scr.height * 2/4)
        elif pos == 'lower left':
            res = (scr.x + scr.width * 1/4, scr.y + scr.height * 3/4)
        elif pos == 'lower center':
            res = (scr.x + scr.width * 2/4, scr.y + scr.height * 3/4)
        elif pos == 'lower right':
            res = (scr.x + scr.width * 3/4, scr.y + scr.height * 3/4)
    else:
        print(f"warning: capture matched a sequence of unknown position type; have you modified the capture rule?")
    return res
