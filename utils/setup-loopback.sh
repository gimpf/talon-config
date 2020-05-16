#!/usr/bin/env bash

# thanks to
# https://askubuntu.com/questions/17791/can-i-downmix-stereo-audio-to-mono
# https://dx9s.net/node/32
# https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/#module-tunnel-sinksource

scarlett_master_input=$(pacmd list-sources | sed -nre 's/\s+name: <(alsa_input.*focusrite.*analog-stereo)>/\1/ip')
scarlett_monitor_output=$(pacmd list-sinks | sed -nre 's/\s+name: <(alsa_output.*focusrite.*analog-stereo)>/\1/ip')

pacmd load-module module-loopback source=scarlett-input-mono sink="${scarlett_monitor_output}" latency_msec=1 rate=44100 # channels=1 channel_map=front-left remix=false

#pacmd load-module module-remap-sink sink_name=scarlett-monitor-mono  sink_properties="device.description=\"Focusrite\ Scarlett\ Solo\ Mono\ Output\""  channels=2 channel_map=mono,mono  master="${scarlett_monitor_output}"  master_channel_map=front-left,front-right  remix=no
#pacmd load-module module-remap-sink sink_name=scarlett-monitor-left  sink_properties="device.description=\"Left\ channel\ of\ Focusrite\ Scarlett\ Solo\ output\""  channels=1 channel_map=front-left  master="${scarlett_monitor_output}"  master_channel_map=front-left  remix=no
#pacmd load-module module-remap-sink sink_name=scarlett-monitor-left  sink_properties="device.description=\"Left\ channel\ of\ Focusrite\ Scarlett\ Solo\ output\""  channels=1 channel_map=front-left  master="${scarlett_monitor_output}"  master_channel_map=front-left  remix=no
#pacmd load-module module-remap-sink sink_name=scarlett-monitor-right sink_properties="device.description=\"Right\ channel\ of\ Focusrite\ Scarlett\ Solo\ output\"" channels=1 channel_map=front-right master="${scarlett_monitor_output}"  master_channel_map=front-right remix=no
#pacmd load-module module-loopback source=scarlett-mono sink=scarlett-monitor-left latency_msec=1 rate=44100 channels=1 channel_map=front-left remix=true
#pacmd load-module module-loopback source=scarlett-mono sink=scarlett-monitor-right latency_msec=1 rate=44100 channels=1 channel_map=front-right remix=true
