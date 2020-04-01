from talon import Module

# prior art: knausj_talon/code/sleep_toggle.py



mod = Module()


@mod.action_class
class Actions:
    def ignore(m: [str]):
        """ignores everything"""
        print(f"ignored phrase: {m}")
