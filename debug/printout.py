from talon import actions, Module

mod = Module()


@mod.action
def print_all_actions():
    """Print all actions to stdout"""
    actions.list()
    # for m in actions._registry.modules:
    #     for act in actions._registry.modules[m]._actions:
    #         print(f'{act}:\t{actions._registry.modules[m]._actions[act].desc}')


@mod.action
def print_all_captures():
    """Print all captures to stdout"""
    for m in actions._registry.modules:
        for c in actions._registry.modules[m]._captures:
            print(f"{c}:\t{actions._registry.modules[m]._captures[c].desc}")


@mod.action
def print_last_phrases():
    """Print last phrases"""
    print(
        "\n".join(
            [f"{i}: {str(x)}" for i, x in enumerate(actions.core.recent_phrases())]
        )
    )
