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

I have a non-native accent, a somewhat noisy environment, and a bad mic.
And I wanted to understand how Talon configurations work.

As a result, I use a different spelling alphabet, always employ prefixed command words, and structure the directories around isolated features instead of large categories.
This makes working with this configuration set slower, but the added redundancy makes it more reliable at correctly recognizing commands.


Should I use this?
-------------------

This configuration is almost unusably incomplete.
Only use it at all if you face the same problems as I do.
Otherwise the community supported configurations will likely be much better for your needs.


About the folder structure
----------------------------

As much as possible, each folder implements only a small number of strongly related features.
The numbers in the folder names only provide sorting for us humans, Talon loads them in arbitrary order.


Other Talon tips
-----------------

### (TODO) Mic Checklist

### Linux

To ensure that some crash is not GPU driver/rendering related, start Talon in software rendering mode by setting the environment variable `LIBGL_ALWAYS_SOFTWARE=1` for the Talon process.


License
--------

Everything is available under the Unlicense, which means as public domain as possible.
See the file [LICENSE](./LICENSE) for details.

If you contribute from other sources, please check that their license is compatible.
(MIT requires attribution in source.)
