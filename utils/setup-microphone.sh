#!/usr/bin/env bash

master_input=$(pacmd list-sources | sed -nre 's/\s+name: <(alsa_input.*focusrite.*analog-stereo)>/\1/ip')
pacmd unload-module module-remap-source
# device.description=\"Left channel of Focusrite Scarlett Solo\"
pacmd load-module module-remap-source source_name=scarlett-mono source_properties="device.description=\"Left\ channel\ of\ Focusrite\ Scarlett\ Solo\"" "master=${master_input}" master_channel_map=front-left channels=1 channel_map=mono
