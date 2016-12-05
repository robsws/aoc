#!/usr/local/bin/python
import sys
import math
import re

file = open("5_input.txt",'r')

total_nice = 0
regex_repeat = re.compile(r"(.{2}).*\1")
regex_xyx = re.compile(r"(.).\1")
for line in file:
  if not re.search(regex_repeat, line):
    continue
  if not re.search(regex_xyx, line):
    continue
  total_nice += 1

print "Total nice strings: "+str(total_nice)