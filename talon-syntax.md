Talon syntax
===========

Commands
---------

* plain word
* optional
* alternatives
* groups
* list
* rule
* start of phrase anchor
* end of phrase anchor

```talon
^[optionally] starting with (group of | alternatives) having a {list} and a <rule> and an end anchor$: write this
```


Actions
--------

* key
  - ctrl
  - ctrl:down
  - ctrl:up
  - a:5
  - ctrl-alt-shift-a
  - ctrl-alt:down a b c d e f ctrl-alt:up
* insert
  - insert("whatever text you like")


```
key(F13): do something
action(user.lol): do something else
voice command: maybe do stuff
voice command with <user.captures>: do stuff with captures
```
