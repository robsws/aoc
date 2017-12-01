#!/usr/local/bin/python
import sys
import math
import re
from operator import add

part = int(sys.argv[1])
input_filename = sys.argv[2]

file = open(input_filename,'r')

for line in file:
  total = 0
  step = len(line)/2
  for i, digit in enumerate(line):
    if part == 1:
      next = i+1
    else:
      next = i+step
    if next >= len(line):
      if part == 1:
        next = 0
      else:
        next = next - len(line)
    if digit == line[next]:
      total = total + int(digit)
  print total