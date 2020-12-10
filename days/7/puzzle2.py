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

# We already have each bag colour added as many times to the list as it needs to be counted
# Again we'll go through each and extend the list
# This could theoretically loop forever if the input data is bad, but, we'll trust that it isn't
inner_bags = bags_in_bag[my_bag]
for colour in inner_bags:
  inner_bags.extend(bags_in_bag[colour])

print(f"A {my_bag} bag must contain a total of {len(inner_bags)} other bags")
