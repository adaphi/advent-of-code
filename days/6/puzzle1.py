#! /usr/bin/env python3

with open("input.txt") as f:
  data = f.read().split('\n\n')

count = 0

for group in data:
  count += len(set([c for c in list(group.replace('\n',''))]))

print(f"The total count is {count}")
