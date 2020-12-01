#! /usr/bin/env python3

import sys

with open("input.txt") as f:
  data = [int(s) for s in f.read().split()]

while data:
  p = data.pop()
  for q, r in [(x, y) for x in data for y in data]:
    if (p+q+r == 2020):
      print(f"{p} + {q} + {r} == 2020")
      print(f"{p} * {q} * {r} == {p*q*r}")
      sys.exit(1)

