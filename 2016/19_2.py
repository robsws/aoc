#!/usr/local/bin/python
import sys
from math import floor
no_of_elves = int(sys.argv[1])

def solve_circle(elves):
  offset = 2
  no_of_elves = len(elves)
  if no_of_elves % 2 == 1:
    offset = 1
  digital_half = int(floor(no_of_elves/2))
  index = digital_half
  next_elves = []
  for i in range(no_of_elves):
    elf = (i+index) % no_of_elves
    if (i-offset) % 3 == 0 or (elf + 1 == digital_half and (no_of_elves % 3 == 1 or no_of_elves % 3 == 2)):
      next_elves.append(elves[elf])
  new_dig_half = int(floor(len(next_elves)/2))
  next_elves = sorted(next_elves)
  return next_elves
  
elves = range(1, no_of_elves+1)
while len(elves) > 1:
  elves = solve_circle(elves)
print(elves)
