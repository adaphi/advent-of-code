#! /usr/bin/env python3

# Did someone say zachlike...

with open("input.txt") as f:
  data = [s.strip() for s in f.readlines()]

line_n = 0
acc = 0
lines_seen = []

# Assuming an infinite loop is guaranteed, this will stop eventually
while line_n not in lines_seen:
  lines_seen.append(line_n)
  line = data[line_n]
  instr, n = line.split()
  if instr == "jmp":
    line_n += int(n)
    continue
  line_n += 1
  if instr == "acc":
    acc += int(n)

print(f"The program terminates after {len(lines_seen)} instructions")
print(f"The accumulator at this point is {acc}")
