#! /usr/bin/env python3

def get_row_num(s):
  return int("0b" + s.translate(str.maketrans({'F': '0', 'B': '1'})), 2)

def get_seat_num(s):
  return int("0b" + s.translate(str.maketrans({'L': '0', 'R': '1'})), 2)

with open("input.txt") as f:
  data = f.readlines()

ids = []

for line in data:
  row = line[:7]
  seat = line[7:]
  row_num = get_row_num(row)
  seat_num = get_seat_num(seat)
  seat_id = (row_num * 8) + seat_num
  ids.append(seat_id)

ids.sort()

for id in ids:
  if (id+1) not in ids and (id+2) in ids:
    print(f"Your seat ID is {id+1}")
    break
