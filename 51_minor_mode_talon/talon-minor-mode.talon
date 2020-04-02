mode: command
mode: dictation
user.minor-mode: talon
-
insert keys:
    insert("key()")
    key(left)

insert insert:
    insert("insert()")
    key(left)

key control: "ctrl"
key alt: "alt"
key shift: "shift"
dash: "-"
space: " "
select word right: key(ctrl-shift-right)
select word left: key(ctrl-shift-left)
