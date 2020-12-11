#! /usr/bin/env python3

with open("input.txt") as f:
  data = [int(s.strip()) for s in f.readlines()]

preamble_length = 25
values = data[:preamble_length]
sums = [a+b for a in values for b in values if a != b]

for n in data[preamble_length:]:
  if n not in sums:
    print(f"The first invalid number is {n}") 
  values.pop(0)
  values.append(n)
  sums = [a+b for a in values for b in values if a != b]
