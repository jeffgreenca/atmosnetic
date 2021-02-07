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
time.sleep(1)
p("quit")
