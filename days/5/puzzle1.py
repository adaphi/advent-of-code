#! /usr/bin/env python3

# We don't need to do anything like the algorithm suggested in the puzzle, these are literally 
# just a description of two binary numbers - one with 7 digits, one with 3

def get_row_num(s):
  return int("0b" + s.translate(str.maketrans({'F': '0', 'B': '1'})), 2)

def get_seat_num(s):
  return int("0b" + s.translate(str.maketrans({'L': '0', 'R': '1'})), 2)

with open("input.txt") as f:
  data = f.readlines()

max_id = 0

for line in data:
  row = line[:7]
  seat = line[7:]
  row_num = get_row_num(row)
  seat_num = get_seat_num(seat)
  seat_id = (row_num * 8) + seat_num
  if (seat_id > max_id):
    max_id = seat_id

print(f"The highest ID in the input is {max_id}")
