#! /usr/bin/env python3

with open("input.txt") as f:
  data = [int(s.strip()) for s in f.readlines()]

jolts = [0] + sorted(data) + [max(data)+3]

diffs = [jolts[i+1] - jolts[i] for i in range(0, len(jolts)-1)]

print(f"There are {diffs.count(1)} 1-jolt differences and {diffs.count(3)} 3-jolt differences")
print(f"The solution is {diffs.count(1) * diffs.count(3)}")
