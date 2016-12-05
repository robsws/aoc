#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

file = open("17_input.txt",'r')

# Parsing
tubs = []
for line in file:
  tubs.append(int(line))

# Work out which combinations of tubs make 150 litres
total_combos = 0
optimal_num_of_containers = 100
optimal_num_of_solutions = 0
for i in range(2 ** len(tubs)):
  binary_num = i + 1
  j = 0
  mask = 1
  total_litres = 0
  num_of_containers = 0
  while j < len(tubs):
    # for each bit
    current_bit = binary_num & mask
    if current_bit == 2 ** j:
      total_litres += tubs[j]
      num_of_containers += 1
    j += 1
    mask = 2 ** j
  if total_litres == 150:
    total_combos += 1
    if num_of_containers < optimal_num_of_containers:
      optimal_num_of_containers = num_of_containers
      optimal_num_of_solutions = 1
    elif num_of_containers == optimal_num_of_containers:
      optimal_num_of_solutions += 1

print optimal_num_of_solutions