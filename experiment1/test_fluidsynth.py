#!/usr/bin/env python3
import time
import random

def p(s):
  print(s, flush=True)

p("prog 1 81")
c=0.02
for n in range(42,68,2):
  v = random.randint(60,110)
  p(f"noteon 1 {n} {v}")
  time.sleep(c)
  p(f"noteoff 1 {n}")
  c += 0.025
time.sleep(0.2)

p("set synth.chorus.level 1")
p("set synth.chorus.speed 2.5")
p("set synth.chorus.active 1")
p("set synth.reverb.room-size 0.5")
p("set synth.reverb.active 1")
p("noteon 1 55 80")
time.sleep(2)
p("noteoff 1 55 80")
time.sleep(2)
p("quit")
