#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

file = open("16_input.txt",'r')

regex = re.compile(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')

# MFCSAM output
mfcsam = {
  "children": 3,
  "cats": 7,
  "samoyeds": 2,
  "pomeranians": 3,
  "akitas": 0,
  "vizslas": 0,
  "goldfish": 5,
  "trees": 3,
  "cars": 2,
  "perfumes": 1
}

# Parsing
sues = []
sues.append({
  "children": 10000,
  "cats": 'na',
  "samoyeds": 'na',
  "pomeranians": 'na',
  "akitas": 'na',
  "vizslas": 'na',
  "goldfish": 'na',
  "trees": 'na',
  "cars": 'na',
  "perfumes": 'na'
})
for line in file:
  match = re.search(regex, line)
  (sue_no, attr1, attr1_value, attr2, attr2_value, attr3, attr3_value,) = match.groups()
  sues.append({
    "children": 'na',
    "cats": 'na',
    "samoyeds": 'na',
    "pomeranians": 'na',
    "akitas": 'na',
    "vizslas": 'na',
    "goldfish": 'na',
    "trees": 'na',
    "cars": 'na',
    "perfumes": 'na'
  })
  sues[int(sue_no)][attr1] = int(attr1_value)
  sues[int(sue_no)][attr2] = int(attr2_value)
  sues[int(sue_no)][attr3] = int(attr3_value)

# check sues against the mfcsam
for i,sue in enumerate(sues):
  badsue = False
  for attr in mfcsam.keys():
    if attr == 'cats' or attr == 'trees':
      if sue[attr] != 'na' and sue[attr] <= mfcsam[attr]:
        badsue = True
        break
    elif attr == 'pomeranians' or attr == 'goldfish':
      if sue[attr] != 'na' and sue[attr] >= mfcsam[attr]:
        badsue = True
        break
    elif sue[attr] != 'na' and sue[attr] != mfcsam[attr]:
      badsue = True
      break
  if not badsue:
    print i