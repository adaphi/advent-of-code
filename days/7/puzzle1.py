#! /usr/bin/env python3

import re

with open("input.txt") as f:
  data = [s.strip() for s in f.readlines()]

# Expecting to need this later
bags_in_bag = {}
bags_containing_bag = {}

rule_re = re.compile(r"([a-z ]+) bags contain (.*)\.")
container_re = re.compile(r"(\d+) ([a-z ]+) bags?")

for line in data:
  colour, contents = rule_re.match(line).groups()
  bags_in_bag[colour] = []
  if contents == "no other bags":
    continue
  for content in contents.split(','):
    c_num, c_colour = container_re.match(content.strip()).groups()
    bags_in_bag[colour].extend([c_colour] * int(c_num))
    if c_colour not in bags_containing_bag:
      bags_containing_bag[c_colour] = set()
    bags_containing_bag[c_colour].add(colour)

my_bag = "shiny gold"
outer_colours = list(bags_containing_bag[my_bag])
# Since this is updating itself, it will keep looping through added colours
# Since it will never contain any colour more than once, the loop will eventually end when it contains all that we need
for colour in outer_colours:
  if colour in bags_containing_bag:
    outer_colours.extend([x for x in bags_containing_bag[colour] if x not in outer_colours])

print(f"A {my_bag} bag could be eventually contained in {len(outer_colours)} possible colours")
