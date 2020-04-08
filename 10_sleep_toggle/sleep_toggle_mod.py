from talon import Module, Context

# prior art: knausj_talon/code/sleep_toggle.py



mod = Module()
mod.setting('noise_enabled', type='bool', desc='Enable callbacks to noise events')
mod.mode('coma', desc='deep sleep where even noises are not handled anymore')

@mod.action_class
class Actions:
    def ignore(m: [str]):
        """ignores everything"""
        print(f"ignored phrase: {m}")
