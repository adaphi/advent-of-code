#! /usr/bin/env python3

with open("input.txt") as f:
  data = f.read().split('\n\n')

count = 0

for group in data:
  answers = [set(x) for x in group.strip().split('\n')]
  count += len(set.intersection(*answers))

print(f"The total count is {count}")
