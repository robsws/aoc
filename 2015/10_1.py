#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

initial_number = sys.argv[1]
iterations = int(sys.argv[2])

def look_and_say(number):
  output = ''
  previous_digit = ''
  current_digit_count = ''
  for digit in number:
    current_digit = digit
    if current_digit == previous_digit:
      current_digit_count += 1
    else:
      output += str(current_digit_count) + previous_digit
      current_digit_count = 1
      previous_digit = current_digit
  output += str(current_digit_count) + previous_digit
  return output

number = initial_number 
for i in range(iterations):
  number = look_and_say(number)
  # print number
 
print len(number)
