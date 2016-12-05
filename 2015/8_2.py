#!/usr/local/bin/python
import sys
import math
import re

file = open("8_input.txt",'r')

total_code_chars = 0
total_encoded_chars = 0

for line in file:
  line = line.replace("\n", "")
  # count the number of code chars in the line
  total_code_chars += len(line)

  print line
  print len(line)

  # replace key chars with encoded representation
  line = line.replace('\\', '\\\\')
  line = line.replace('"', '\\"')
  line = '"'+line+'"'

  # count the number memory chars after replacement
  total_encoded_chars += len(line)
  
  print line
  print len(line)

print total_encoded_chars - total_code_chars