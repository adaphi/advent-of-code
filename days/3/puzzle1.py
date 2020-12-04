#! /usr/bin/env python3

with open("input.txt") as f:
  spaces = [line[i*3 % len(line.strip())] for i, line in enumerate(f)]

print(f"You would hit {spaces.count('#')} trees")
