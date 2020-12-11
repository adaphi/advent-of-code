#! /usr/bin/env python3

# Did someone say zachlike...

# We could investigate potential programs one by one by
# changing a single instruction and re-executing, but that's dull
# Instead let's execute it just once, but with backtracking!

def save_state():
  global line_n, acc, lines_seen
  global backtrack_active, saved_line_n, saved_acc, saved_lines_seen
  saved_line_n = line_n
  saved_acc = acc
  saved_lines_seen = list(lines_seen)
  backtrack_active = True

def restore_state():
  global line_n, acc, lines_seen
  global backtrack_active, saved_line_n, saved_acc, saved_lines_seen
  line_n = saved_line_n
  acc = saved_acc
  lines_seen = list(saved_lines_seen)
  backtrack_active = False

with open("input.txt") as f:
  data = [s.strip() for s in f.readlines()]

line_n = 0
acc = 0
lines_seen = []

backtrack_active = False

# This condition will stop execution at exactly the
# right spot, so we need to take care of other edge cases
# in the loop
while line_n != len(data):
  lines_seen.append(line_n)
  line = data[line_n]
  instr, n = line.split()

  if instr == "acc":
    acc += int(n)
    line_n += 1
    continue

  if instr == "jmp":
    line_n += int(n)
  else:
    line_n += 1

  # jmp and nop instructions will put the "real" instruction
  # in the backtrack vars, and follow the alternate path first
  # but we only do this for one instruction in the program at a time
  if not backtrack_active and instr in ["jmp", "nop"]:
    save_state()
    if instr == "jmp":
      line_n += 1 - int(n)
    else:
      line_n += int(n) - 1

  # This time we need some checks to make sure the loop is OK
  if line_n in lines_seen or line_n < 0 or line_n > len(data):
    # Restoring will put us on whatever the next line would have been, had we not changed things
    restore_state()

print(f"The program completes after changing line {saved_lines_seen[-1]}")
print(f"The accumulator at this point is {acc}")
