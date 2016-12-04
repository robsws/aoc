#!/usr/local/bin/python
from operator import itemgetter
import re

file = open("4_input.txt",'r')
regex = re.compile(r"^(.*)-(\d+)\[(\w+)\]$")

def build_checksum(code):
  # Get the 5 most common letters and output as a string.
  # In ties, output letters in alphabetical order.
  # First, count the letters in the code.
  letters = {}
  for char in code:
    if char in letters:
      letters[char] += 1
    else:
      letters[char] = 1
  # Sort the letters dict first alphabetically by key
  # and then by occurrences (yielding a list of tuples like ('g',2) )
  tmp_letters = sorted(letters.items(), key=itemgetter(0))
  sorted_letters = sorted(tmp_letters, key=itemgetter(1), reverse=True)
  # Build the 5 character string and return.
  checksum = ''
  for i in range(5):
    checksum += sorted_letters[i][0]
  return checksum

total = 0
for line in file:
  match = re.search(regex, line)
  (code, sector_id, checksum) = match.groups()
  code = code.replace('-','')
  calculated_checksum = build_checksum(code)
  if checksum == calculated_checksum:
    total += int(sector_id)
print(total)