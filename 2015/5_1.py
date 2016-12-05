#!/usr/local/bin/python
import sys
import math
import re

file = open("5_input.txt",'r')

total_nice = 0
regex_vowels = re.compile(r".*[aeiou].*[aeiou].*[aeiou].*")
regex_doubles = re.compile(r"(.)\1")
regex_disallowed = re.compile(r"ab|cd|pq|xy")
for line in file:
  if not re.search(regex_vowels, line):
    continue
  if not re.search(regex_doubles, line):
    continue
  if re.search(regex_disallowed, line):
    continue
  total_nice += 1

print "Total nice strings: "+str(total_nice)