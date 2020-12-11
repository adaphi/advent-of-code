#! /usr/bin/env python3

# Conway's waiting area

with open("input.txt") as f:
  data = [s.strip() for s in f.readlines()]

seats = {(x,y): {"is_chair": c == "L", "occupied": False} for x, line in enumerate(data) for y, c in enumerate(line)}

# grmbl this was nice and easy before
for k, s in seats.items():
  if not s["is_chair"]:
    continue
  x, y = k
  seats[k]["seen"] = []
  for dx, dy in ((a,b) for a in [-1, 0, 1] for b in [-1, 0, 1] if not (a == 0 and b == 0)):
    vis = next((seats[z] for z in ((x+n*dx, y+n*dy) for n in range(1,len(seats))) if z in seats and seats[z]["is_chair"]), None)
    if vis is not None:
      seats[k]["seen"].append(vis)

changes = ["init"]
while len(changes) > 0:
  changes = []
  # Logic pass first, don't change anything
  for s in seats.values():
    if not s["is_chair"]:
      continue
    if not s["occupied"] and not any(x["occupied"] for x in s["seen"]):
      changes.append((s, {"occupied": True}))
    elif s["occupied"] and len([x for x in s["seen"] if x["occupied"]]) >= 5:
      changes.append((s, {"occupied": False}))

  # Now update
  for seat, change in changes:
    seat.update(change)

total_occupied = len([s for s in seats.values() if s["is_chair"] and s["occupied"]])

print(f"When settled, there are {total_occupied} occupied seats.")
