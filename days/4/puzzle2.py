#! /usr/bin/env python3

import re

re_year = re.compile(r"^\d{4}$")
re_height = re.compile(r"^\d{2,3}(in|cm)$")
re_hcl = re.compile(r"^#[0-9a-f]{6}$")
re_pid = re.compile(r"^\d{9}$")

data = []

def is_valid_passport(passport):
  valid_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

  if any(key not in passport for key in valid_keys):
    return False

  if not (re_year.match(passport["byr"]) and 1920 <= int(passport["byr"]) <= 2002):
    return False

  if not (re_year.match(passport["iyr"]) and 2010 <= int(passport["iyr"]) <= 2020):
    return False

  if not (re_year.match(passport["eyr"]) and 2020 <= int(passport["eyr"]) <= 2030):
    return False

  if not re_height.match(passport["hgt"]):
    return False
  else:
    if passport["hgt"].endswith("cm") and not 150 <= int(passport["hgt"][:-2]) <= 193:
      return False
    if passport["hgt"].endswith("in") and not 59 <= int(passport["hgt"][:-2]) <= 76:
      return False

  if not re_hcl.match(passport["hcl"]):
    return False

  if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
    return False

  if not re_pid.match(passport["pid"]):
    return False

  return True


# Program start

with open("input.txt") as f:
  data = [dict(s.split(':') for s in x.split()) for x in f.read().split('\n\n')]

valid_passports = [p for p in data if is_valid_passport(p)]

print(f"There are {len(valid_passports)} valid passports in the file")
