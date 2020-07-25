from os import system

from talon import app, imgui, Module, actions
from talon.engine import engine

show_notifications = True
hist_len = 10
history = []


def parse_phrase(phrase):
    return ' '.join(word.split('\\')[0] for word in phrase)


def on_phrase_post(j):
    global hist_len
    global history

    phrase = getattr(j['parsed'], '_unmapped', j['phrase'])
    phrase = parse_phrase(phrase)
    cmd = j['cmd']
    if cmd == 'p.end' and phrase:
        if show_notifications:
            app.notify(body=phrase)
        history.append(phrase)
        history = history[-hist_len:]
        # theoretically, this is necessary, practically, it is not, but ... ???
        if gui.showing:
            gui.freeze()

# todo: dynamic rect?
@imgui.open(y=0, x=0, software=True)
def gui(gui: imgui.GUI):
    gui.text("Command History")
    gui.line()
    text = history[:]
    # text = [str(x) for x in actions.core.recent_phrases()[:hist_len]]
    for line in text:
        gui.text(line)


engine.register('post:phrase', on_phrase_post)

mod = Module()
@mod.action_class
class Actions:
    def history_enable():
        """Enables the history"""
        gui.freeze()

    def history_disable():
        """Disables the history"""
        gui.hide()

    def history_clear():
        """Clear the history"""
        global history
        history = []
