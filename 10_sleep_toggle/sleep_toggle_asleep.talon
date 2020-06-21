mode: sleep
-
settings():
    user.noise_enabled = 'True'

^talon wake up gently$:
    speech.enable()
    mode.restore()
    # the following is a workaround while 'noise' mode isn't finished yet
    mode.disable('user.coma')

# to make spurious wake-ups more rare (because talon tries too hard to match the audio to
# the only existing command - which is wake-up), have an ignore-all match for any number of
# any words; this makes the above command require higher confidence to actually trigger.
<word>+:
    skip()
