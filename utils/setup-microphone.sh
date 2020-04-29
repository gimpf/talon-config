#!/usr/bin/env bash

# thanks to
# https://askubuntu.com/questions/17791/can-i-downmix-stereo-audio-to-mono
# https://dx9s.net/node/32

master_input=$(pacmd list-sources | sed -nre 's/\s+name: <(alsa_input.*focusrite.*analog-stereo)>/\1/ip')
pacmd unload-module module-remap-source

pacmd load-module module-remap-source source_name=scarlett-mono source_properties="device.description=\"Left\ channel\ of\ Focusrite\ Scarlett\ Solo\"" "master=${master_input}" master_channel_map=front-left rate=44100 channels=1 channel_map=mono remix=no
