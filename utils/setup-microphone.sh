#!/usr/bin/env bash

# thanks to
# https://askubuntu.com/questions/17791/can-i-downmix-stereo-audio-to-mono
# https://dx9s.net/node/32
# https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/#module-tunnel-sinksource

scarlett_master_input=$(pacmd list-sources | sed -nre 's/\s+name: <(alsa_input.*focusrite.*analog-stereo)>/\1/ip')
scarlett_monitor_output=$(pacmd list-sinks | sed -nre 's/\s+name: <(alsa_output.*focusrite.*analog-stereo)>/\1/ip')

echo Monoize...
pacmd load-module module-remap-source \
    source_name=scarlett-input-mono \
    source_properties="device.description=\"Left\ channel\ of\ Focusrite\ Scarlett\ Solo\"" \
    "master=${scarlett_master_input}" \
    master_channel_map=front-left \
    channels=1 \
    channel_map=mono \
    remix=no \
    # rate=44100 \

# echo Nullify...
# pacmd load-module module-null-sink \
#     sink_name=null-sink
#
# echo Compress...
# pacmd load-module module-ladspa-sink \
#       sink_name=scarlett-in-mono-calf_comp_x2 \
#       sink_properties="device.description=\"Compressed\ Left\ channel\ of\ Focusrite\ Scarlett\ Solo\"" \
#       sink_master=null-sink \
#       plugin=calf \
#       label=Compressor \
#       control=",1,0.032,3,25,75,,,,"
#       # see https://wiki.archlinux.org/index.php/PulseAudio#Calf_plugin
#       # bypass (def 0, [0,1], bool)
#       # level in (def 1, [0.015625, 64], float dB)
#       # threshold (def 0.125, [0.000976563, 1], float dBFS, -18 dB -> 10^(-18/20) = 0.158, -30dB = 0.032)
#       # ratio (def 2, [1,20], float)
#       # attack (def 20, [0.01, 2000], float ms)
#       # release (def 250, [0.01, 2000], float ms)
#       # makeup (def 1, [1,64], float dB)
#       # knee (def 2.828427125, [1,8], float dB)
#       # rms/peak (def 0, 0|1, bool, 0 = rms, 1 = peak)
#       # stereo link (def 0, 0|1, bool, 0 = avg, 1 = max)
#       # mix (def 1, [0,1], float %)
#
# echo Bind...
# pacmd load-module module-loopback \
#     source=scarlett-input-mono \
#     sink=scarlett-in-mono-calf_comp_x2 \
#     latency_msec=1 \
#     # rate=44100 \
#     # channels=1 \
#     # channel_map=front-left \
#     # remix=false
#
# echo Fix default sink...
# pacmd set-default-sink ${scarlett_monitor_output}
