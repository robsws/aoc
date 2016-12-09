#!/usr/local/bin/python
import sys
import re

(prog, filename) = sys.argv
file = open(filename,'r')
marker_pattern = re.compile(r"^(\((\d+)x(\d+)\))")

def decompress(data):
  decompressed = ''
  while(len(data) > 0):
    match = re.search(marker_pattern, data)
    if match:
      (marker, amount, multiplier) = match.groups()
      amount = int(amount)
      multiplier = int(multiplier)
      data_to_repeat = data[len(marker):len(marker)+amount]
      data_to_repeat = decompress(data_to_repeat)
      repeated_data = data_to_repeat * multiplier
      decompressed += repeated_data
      data = data[len(marker)+amount:]
    else:
      decompressed += data[0]
      data = data[1:]
  return decompressed

data = ''
for line in file:
  line = line.rstrip()
  data += line

print(len(decompress(data)))
