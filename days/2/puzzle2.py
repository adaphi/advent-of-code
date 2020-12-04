#! /usr/bin/env python3

# Of course the original requirements were wrong
#def isGoodPassword(policy, letter, password):
#  policyMin, policyMax = policy.split('-')
#  letter = letter.strip(':')
#  return int(policyMin) <= password.count(letter) <= int(policyMax)

def isGoodPassword(policy, letter, password):
  # Subtract 1 as these aren't 0-indexed
  policyFirst, policyLast = [int(s)-1 for s in policy.split('-')]
  letter = letter.strip(':')
  return (
    (password[policyFirst] == letter or password[policyLast] == letter)
    and password[policyFirst] != password[policyLast]
  )

with open('input.txt') as f:
  goodPasswords = [line for line in f if isGoodPassword(*line.split())]

print(f"There are {len(goodPasswords)} good password(s)")
