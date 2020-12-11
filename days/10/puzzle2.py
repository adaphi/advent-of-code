#! /usr/bin/env python3

with open("input.txt") as f:
  data = [int(s.strip()) for s in f.readlines()]

jolts = [0] + sorted(data) + [max(data)+3]

diffs = [jolts[i+1] - jolts[i] for i in range(0, len(jolts)-1)]

# So this is combinatorics, but not quite
# Any time an adapter can only connect to one other adapter,
# they must always be together, so they don't affect the number of combinations.
# The only adapters we care about are the ones that have a choice of
# whether to use them or not.
# At first it seems like you can just count and multiply the choices,
# but this overcounts, as some choices eliminate others.
#
# The hint from part 1 is to look at the differences between the numbers.
# Any time we can add one or more of these numbers together and get <=3,
# that is a place where one or more adapters could be left out, i.e. a separate potential
# combination.
# Note that this means that points where there is a diff of 3 break the chain into
# independent pieces, so we can count combinations separately for these pieces and multiply together.
# Counting those pieces would take a long time for large lists without a trick or two
# But these aren't that large, so we'll just crunch them

def listpartition(l, sep):
  i=0
  while sep in l[i:]:
    j = l.index(sep, i)
    yield tuple(l[i:j])
    #yield (l[j],)
    i = j+1

def pairwise(l):
  return ( l[:i] + (l[i] + l[i+1],) + l[i+2:] for i in range(0, len(l)-1) if l[i] + l[i+1] <= 3 )

arrangements = 1

for sublist in listpartition(diffs, 3):
  if len(sublist) == 1:
    continue
  sub_arrangements = set()
  to_check = [sublist]
  while len(to_check) > 0:
    sub_arrangements.update(to_check)
    temp = []
    for l in to_check:
      temp.extend(pairwise(l))
    to_check = temp
  arrangements *= len(sub_arrangements)


print(f"There are {arrangements} possible arrangements")
