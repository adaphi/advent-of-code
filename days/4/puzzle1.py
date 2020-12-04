#! /usr/bin/env python3

data = []
with open("input.txt") as f:
  data = [dict(s.split(':') for s in x.split()) for x in f.read().split('\n\n')]

valid_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid_passports = [p for p in data if all(key in p for key in valid_keys)]

print(f"There are {len(valid_passports)} valid passports in the file")
