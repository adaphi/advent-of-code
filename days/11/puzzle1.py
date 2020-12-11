#! /usr/bin/env python3

# Conway's waiting area

with open("input.txt") as f:
  data = [s.strip() for s in f.readlines()]

seats = {(x,y): {"is_chair": c == "L", "occupied": False} for x, line in enumerate(data) for y, c in enumerate(line)}

for k in seats.keys():
  x, y = k
  seats[k]["adjacent"] = [seats[z] for z in ((x+a,y+b) for a in [-1, 0, 1] for b in [-1, 0, 1] if not (a == 0 and b == 0)) if z in seats]

changes = ["init"]
while len(changes) > 0:
  changes = []
  # Logic pass first, don't change anything
  for s in seats.values():
    if not s["is_chair"]:
      continue
    if not s["occupied"] and not any(x["occupied"] for x in s["adjacent"]):
      changes.append((s, {"occupied": True}))
    elif s["occupied"] and len([x for x in s["adjacent"] if x["occupied"]]) >= 4:
      changes.append((s, {"occupied": False}))

  # Now update
  for seat, change in changes:
    seat.update(change)

total_occupied = len([s for s in seats.values() if s["is_chair"] and s["occupied"]])

print(f"When settled, there are {total_occupied} occupied seats.")
