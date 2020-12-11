#! /usr/bin/env python3

with open("input.txt") as f:
  data = [int(s.strip()) for s in f.readlines()]

target = 1492208709
for i, n in enumerate(data):
   current = n
   j = i+1
   while current < target:
     current += data[j]
     j += 1
   if current == target:
     break

target_range = data[i:j]
print(f"The weakness is {min(target_range) + max(target_range)}")
