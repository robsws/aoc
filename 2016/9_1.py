#!/usr/local/bin/python
import sys
import re

(prog, filename) = sys.argv
file = open(filename,'r')
marker_pattern = re.compile(r"^(\((\d+)x(\d+)\))")

decompressed_length = 0
for line in file:
  line = line.rstrip()
  while(len(line) > 0):
    match = re.search(marker_pattern, line)
    if match:
      # Found a marker
      (marker, amount, multiplier) = match.groups()
      amount = int(amount)
      multiplier = int(multiplier)
      decompressed_length += amount * multiplier
      line = line[len(marker) + amount:]
    else:
      decompressed_length += 1
      line = line[1:]
print(decompressed_length)