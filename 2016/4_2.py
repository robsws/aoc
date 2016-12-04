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
    if char == '-':
      continue
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

def shift_char(char, amount):
  if ord(char) + amount > ord('z'):
    return chr(ord('a')-1 + (ord(char) + amount - ord('z')))
  else:
    return chr(ord(char) + amount)

def caesar_shift(code, amount):
  decoded = ''
  amount = amount % 26
  for char in code:
    if char == '-':
      decoded += ' '
    else:
      decoded += shift_char(char, amount)
  return decoded

north_pole_regex = re.compile(r"north")

for line in file:
  match = re.search(regex, line)
  (code, sector_id, checksum) = match.groups()
  calculated_checksum = build_checksum(code)
  if checksum == calculated_checksum:
    sector = caesar_shift(code, int(sector_id)) + ": " + sector_id
    if re.search(north_pole_regex, sector):
      print(sector)