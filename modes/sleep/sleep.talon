mode: sleep
not user.minor-mode: /coma/
-
settings():
    user.noise_enabled = 1

# to make spurious wake-ups more rare (because talon tries too hard to match the audio to
# the only existing command - which is wake-up), have an ignore-all match for any number of
# any words; this makes the wake up commands require higher confidence to actually trigger.
<word>+:
   skip()
