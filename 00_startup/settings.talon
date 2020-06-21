settings():
    # increased the size of Talon UI, like help
    imgui.scale = 1.3
    # delay used for simulated key-presses, in ms; is used multiple times during a single press!
    # 5 is crazy slow, most go with 1 or 1.5
    key_wait = 5
    # delay between separate characters in insert(), in ms
    # 20 is crazy slow, 5 suffices for most
    insert_wait = 20
