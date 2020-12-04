#! /usr/bin/env python3

import sys

with open("input.txt") as f:
  data = [int(s) for s in f.read().split()]

while data:
  p = data.pop()
  for q in data:
    if (p+q == 2020):
      print(f"{p} + {q} == 2020")
      print(f"{p} * {q} == {p*q}")
      sys.exit(1)

