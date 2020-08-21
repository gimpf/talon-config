os: linux
app: Xfce4-terminal
-
tag(): user.tabs
tag(): user.windows
tag(): user.generic-tabs
tag(): user.terminal

#### Tabs

action(app.tab_close):  key(ctrl-shift-w)
action(app.tab_detach): key(ctrl-shift-d)
action(app.tab_open):   key(ctrl-shift-t)

#### Windows

action(app.window_open): key(ctrl-shift-n)
action(app.window_close): key(ctrl-shift-q)
