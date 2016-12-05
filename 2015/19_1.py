#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

file = open("19_input.txt",'r')

# Parsing
mappings = {}
regex = re.compile(r'(\w+) => (\w+)')
final_line = False
input_molecule = ''
for line in file:
  if final_line:
    input_molecule = line
  match = re.search(regex, line)
  if match:
    if match.group(1) not in mappings.keys():
      mappings[match.group(1)] = []
    mappings[match.group(1)].append(match.group(2))
  else:
    final_line = True
  
# Distinct molecules created by applying each mapping one at a time
molecules = {}
for element in mappings.keys():
  for conversion in mappings[element]:
    for match in re.finditer(element, input_molecule):
      # splice new molecule
      molecule = input_molecule[:match.start()] + conversion + input_molecule[match.end():]
      print element+" => "+conversion
      print molecule
      if molecule not in molecules.keys():
        molecules[molecule] = 0
      molecules[molecule] += 1

print len(molecules.keys())
