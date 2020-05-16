#!/usr/bin/env bash

pacmd unload-module module-remap-source
pacmd unload-module module-remap-sink
pacmd unload-module module-null-sink
pacmd unload-module module-ladspa-sink
pacmd unload-module module-loopback
