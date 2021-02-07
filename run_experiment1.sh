#!/bin/bash
. env.sh
./experiment1/test_fluidsynth.py | fluidsynth -a pulseaudio -g 1.0 $SF_GS
