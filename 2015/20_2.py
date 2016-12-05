#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

target_presents = 36000000

presents = [0 for x in range(3600000)]
for elf in range(1, 3600000):
  for i in range(1, 51):
    house = elf * i
    if house < 3600000:
      presents[house] += 11 * elf

most = 0
for house,number in enumerate(presents):
  if number > most:
    most = number
  if number > target_presents:
    print house
    print number
    break

print most