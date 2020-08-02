from talon import Module, Context

mod = Module()
mod.setting(
    "noise_enabled", type=int, default=0, desc="Enable callbacks to noise events"
)
