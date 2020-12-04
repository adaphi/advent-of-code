#! /usr/bin/env python3

def isGoodPassword(policy, letter, password):
  policyMin, policyMax = policy.split('-')
  letter = letter.strip(':')
  return int(policyMin) <= password.count(letter) <= int(policyMax)

with open('input.txt') as f:
  goodPasswords = [line for line in f if isGoodPassword(*line.split())]

print(f"There are {len(goodPasswords)} good password(s)")
