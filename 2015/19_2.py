#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

file = open("19_input.txt",'r')

# Parsing
mappings = {}
reverse_mappings = {}
regex = re.compile(r'(\w+) => (\w+)')
final_line = False
molecule = ''
for line in file:
  if final_line:
    molecule = line
  match = re.search(regex, line)
  if match:
    if match.group(1) not in mappings.keys():
      mappings[match.group(1)] = []
    mappings[match.group(1)].append(match.group(2))
    reverse_mappings[match.group(2)] = match.group(1)
  else:
    final_line = True

# Rules are all of following format:
# 1. X -> X X
# 2. X -> X ( X )
# 3. X -> X ( X , X [, X ...] )

molecule = re.sub('\n','',molecule)
conversions = 0
# Step 1 - convert all terminals and non-terminals to uniform symbols
terminal_regex = re.compile(r'\(|\)|,')
non_terminal_regex = re.compile(r'([A-Z][a-z]?)')
molecule = re.sub('Rn','(',molecule)
molecule = re.sub('Y',',',molecule)
molecule = re.sub('Ar',')',molecule)
molecule = re.sub(non_terminal_regex, 'X', molecule)

conversions = 0
while len(molecule) > 1:
  conversions += 1
  match = re.search(r'(XX)', molecule)
  if match:
    molecule = molecule[:match.start()] + 'X' + molecule[match.end():]
    continue
  match = re.search(r'(X\(X(,X)*\))', molecule)
  if match:
    molecule = molecule[:match.start()] + 'X' + molecule[match.end():]
    continue
  break
print molecule
print conversions