#!/usr/local/bin/python
import sys
import re

(prog, filename) = sys.argv
file = open(filename,'r')
marker_pattern = re.compile(r"^(\((\d+)x(\d+)\))")

def decompress(data):
  # Gradually search character by character through a data string for a marker.
  # If one is found, decompress the next x characters (defined by the marker)
  # and then repeat the whole decompressed string y number of times (defined by
  # the marker).
  decompressed = ''
  while(len(data) > 0):
    match = re.search(marker_pattern, data)
    if match:
      # Found marker
      (marker, amount, multiplier) = match.groups()
      amount = int(amount)
      multiplier = int(multiplier)
      # Recurse on the next x characters
      data_to_repeat = decompress(data[len(marker):len(marker)+amount])
      # Repeat the decompressed string y number of times
      decompressed += data_to_repeat * multiplier
      # Eat the marker and x characters from the input
      data = data[len(marker)+amount:]
    else:
      # No marker, eat one character from the input and append it to the output.
      decompressed += data[0]
      data = data[1:]
  return decompressed

data = ''
for line in file:
  data += line.rstrip()

print(len(decompress(data)))
