#!/usr/local/bin/python
import sys
import math
import re

file = open("12_input.txt",'r')

regex = re.compile(r'(-?[0-9]+)')
sum_of_numbers = 0
for line in file:
  for match in re.finditer(regex, line):
    sum_of_numbers += int(match.group(1))

print sum_of_numbers