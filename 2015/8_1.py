#!/usr/local/bin/python
import sys
import math
import re

file = open("8_input.txt",'r')

total_code_chars = 0
total_mem_chars = 0

escaped_regex = re.compile(r'\\(\\|\"|x[0-9a-zA-Z]{2})')
quotes_regex = re.compile(r'^\"(.*)\"$')

for line in file:
  # count the number of code chars in the line
  total_code_chars += len(line) - 1
  # replace escaped chars with memory representation
  match = re.match(quotes_regex, line)
  processed_line = match.group(1)
  processed_line = re.sub(escaped_regex, '~', processed_line)

  # count the number memory chars after replacement
  total_mem_chars += len(processed_line)
  print line
  print len(line) - 1
  print processed_line
  print len(processed_line)
  print ' '

print total_code_chars - total_mem_chars