from talon import Context, Module, actions, cron, imgui, settings

mod = Module()

mod.mode('tutu_none', desc='show a mode')
mod.mode('tutu_one', desc='show a mode')
mod.mode('tutu_two', desc='show a mode')
mod.setting('latest_name', type=str, desc='latest_name', default='hugo')

my_scope = set()

@imgui.open(y=100, software=True)
def illustrated_ui(gui: imgui.GUI):
    gui.text(f"latest tutu: {settings.get('self.latest_name')}")


@mod.scope
def scope():
    return {'tutu': my_scope}

@mod.action
def enable_tutu(t: str):
    "enable tutu"
    my_scope.add(t)
    scope.update()

@mod.action
def disable_tutu(t: str):
    "disable tutu"
    if t in my_scope:
        my_scope.remove(t)
    scope.update()

@mod.action
def show_no_tutu():
    "be nothing"
    actions.mode.disable("user.tutu_one")
    actions.mode.disable("user.tutu_two")
    actions.user.disable_tutu("one")
    actions.user.disable_tutu("two")
    illustrated_ui.freeze()

@mod.action
def show_tutu_one():
    "provide one"
    actions.mode.disable("user.tutu_two")
    actions.mode.enable("user.tutu_one")
    actions.user.disable_tutu("two")
    actions.user.enable_tutu("one")
    illustrated_ui.freeze()

@mod.action
def show_tutu_two():
    "provide two"
    actions.mode.disable("user.tutu_one")
    actions.mode.enable("user.tutu_two")
    actions.user.disable_tutu("one")
    actions.user.enable_tutu("two")
    illustrated_ui.freeze()

ctx_none = Context()
ctx_none.settings["user.latest_name"] = "none"
ctx_none.defines = r'''
^illustrate nothing$:
    user.show_no_tutu()

^illustrate one$:
    user.show_tutu_one()

^illustrate two$:
    user.show_tutu_two()
'''

ctx_one = Context()
ctx_one.matches = r'''
user.tutu: one
# mode: tutu_one
'''
ctx_one.settings["user.latest_name"] = "one"

ctx_two = Context()
ctx_two.matches = r'''
user.tutu: two
# mode: tutu_two
'''
ctx_two.settings["user.latest_name"] = "two"
