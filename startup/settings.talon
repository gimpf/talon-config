settings():
    # increased the size of Talon UI, like help
    imgui.scale = 1.3
    # delay used for simulated key-presses, in ms; is used multiple times during a single press!
    # 5 is crazy slow, most go with 1 or 1.5
    key_wait = 5
    # delay between separate characters in insert(), in ms
    # 20 is crazy slow, 5 suffices for most
    insert_wait = 20
    # delay used for ... keeping keys held?
    # key_hold =
    # (unstable) threshold for VAD (voice activity detector), default 0.75
    #speech.threshold = 0.75
    # (unstable) minimum silence time before speech is cut off, default 0.150
    speech.timeout = 0.200
    # (unstable) print out additional VAD etc. data to stdout, not log, default 0
    speech.debug = 0
