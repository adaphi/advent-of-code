#! /usr/bin/env python3

with open("input.txt") as f:
  data = [s.strip() for s in f.readlines()]

slopes = [
  (1,1),
  (3,1),
  (5,1),
  (7,1),
  (1,2)
]

answer = 1

for dx, dy in slopes:
  # Fetch all the lines we will actually hit (some will be skipped if dy > 1)
  lines = [line for i, line in enumerate(data) if i % dy == 0]
  # Re-index those lines and get the appropriate character from each
  spaces = [line[i*dx % len(line)] for i, line in enumerate(lines)]
  print(f"On slope ({dx}, {dy}), you would hit {spaces.count('#')} trees")
  answer *= spaces.count('#')

print(f"Multiplied together, this gives {answer}")
