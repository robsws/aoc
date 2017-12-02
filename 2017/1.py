#!/usr/local/bin/python
import sys
from itertools import tee, cycle

part = int(sys.argv[1])
input_filename = sys.argv[2]
file = open(input_filename,'r')

# Loops through pairs of elements in a list
# that are offset by a given amount
def pairs(iterable, step):
    # Make two iterators over the list
    a, b = tee(iterable)
    # Offset second iterator by step and loop it round to beginning
    c = cycle(b)
    for i in range(step):
      next(c)
    # Make iterator that returns results as tuples
    return zip(a, c)

for line in file:
  line = line.rstrip("\n")
  if part == 1:
    step = 1
  else:
    step = int(len(line)/2)
  # Convert to integer list
  line = map(int, line)
  # Sum the list elements for which the offset element is equal
  total = sum([ pair[0] for pair in pairs(line, step) if pair[0] == pair[1] ])
  print(total)