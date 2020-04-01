from talon import actions, Module

mod = Module()

@mod.action_class
class Actions:
    def print_all_actions():
        """Print all actions to stdout"""
        actions.list()
        # for m in actions._registry.modules:
        #     for act in actions._registry.modules[m]._actions:
        #         print(f'{act}:\t{actions._registry.modules[m]._actions[act].desc}')

    def print_all_captures():
        """Print all captures to stdout"""
        for m in actions._registry.modules:
            for c in actions._registry.modules[m]._captures:
                print(f'{c}:\t{actions._registry.modules[m]._captures[c].desc}')
