Talon Config
================

What is this?
--------------

[Talon Voice](https://talonvoice.com/) is a computer voice control engine that i.a. aims to bring _"full desktop computer proficiency to people who have limited or no use of their hands"_, developed by [lunixbochs](https://github.com/lunixbochs/).

To make use of it, you need to provide a configuration for the engine.
There are several ready-to-use configurations available, like [knausj_talon](https://github.com/knausj85/knausj_talon) for the beta version or [2shea's start pack](https://github.com/2shea/talon_starter_pack) for the release version.

This repository is another configuration set, based upon a heavily modified [knausj_talon](https://github.com/knausj85/knausj_talon), taking bits and pieces from the [talonvoice examples](https://github.com/talonvoice/examples), as well as some snippets from the Slack channel.


Why another configuration set?
-------------------------------

I have a non-native accent, a somewhat noisy environment, and the wrong mic for the job.
And I wanted to understand how Talon configurations work.

As a result, I use a different spelling alphabet, always employ prefixed command words, and structure the directories around isolated features instead of large categories.
The changed alphabet and commands make working with this configuration set slower, but the added redundancy makes for a bit more reliable recognition.


Should I use this?
-------------------

This configuration is almost unusably incomplete.
Only use it at all if you face the same problems as I do.
Otherwise the community supported configurations will very likely be much better for your needs.


About the folder structure
----------------------------

As much as possible, each folder implements only a small number of strongly related features.
The numbers in the folder names only provide sorting for us humans, Talon loads them in arbitrary order.


Other Talon tips
-----------------

### Linux

* ImGUI issues: for some linux distributions, ImGUI will crash Talon with a segmentation fault after a few times of using help and/or command history.
  For this, I set `software=True` in the `imgui` annotations.
  Were this not Mesa related but a driver issue, using software rendering by setting the environment variable `LIBGL_ALWAYS_SOFTWARE=1` were also an option.


Talon Getting Started and Documention
--------------------------------------

* https://whalequench.club/blog/2019/09/03/learning-to-speak-code.html

### Talon Modes

Talon supports so called modes.
Such modes are like a context for contexts:
Some contexts (in .py or .talon files) may be available only for a few or a single mode.
As a result, each mode can have a unique set of commands available for the user.

In a .py file, use `ctx.matches = 'mode: all'` to set the mode, in a talon file add a line `mode: all` to the header.

* `command`: activates voice commands
* `hotkey`: activates hotkey commands
* `noise`: activates noise commands
* `dictation`: when using voice primarily for dictating text instead of issuing command
* `sleep`: while sleeping
* `dragon`: activates dragon naturally speaking dicatation mode

```
mode.enable(name)
mode.disable(name)
mode.toggle(name)
mode.save()
mode.restore()
speech.disable()
speech.enable()
mod.mode('name', desc='this is what the mode is for')
```


List of Talon config-sets
--------------------------

* https://github.com/knausj85/knausj_talon - The "go-to" beta version config-set
* https://github.com/dwiel/talon_community
* https://github.com/jcaw/talon_config
* https://github.com/lunixbochs/talon_starter_pack
* https://github.com/2shea/talon_starter_pack
* https://github.com/2shea/talon_configs
* https://github.com/talonvoice/examples
* https://github.com/anonfunc/talon-user


License
--------

Everything is available under the Unlicense, which means as public domain as possible.
See the file [LICENSE](./LICENSE) for details.

If you contribute from other sources, please check that their license is compatible.
(MIT requires attribution in source.)
