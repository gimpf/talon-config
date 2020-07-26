from talon import Module, Context

mod = Module()
mod.setting('noise_enabled', type=bool, desc='Enable callbacks to noise events')
mod.mode('coma', desc='deep sleep where even noises are not handled anymore')
