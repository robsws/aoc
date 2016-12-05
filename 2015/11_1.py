#!/usr/local/bin/python
import sys
import math
import re

previous_password = sys.argv[1]

def increment_password(password):
  final_char_index = len(password) - 1
  final_char = password[final_char_index]
  if final_char == 'z':
    return increment_password(password[0:final_char_index]) + 'a'
  else:
    final_char = chr(ord(final_char) + 1)
    return password[0:final_char_index] + final_char

regex_disallowed = re.compile(r"i|o|l")
regex_doubles = re.compile(r"(.)\1.*(.)\2")
def valid_password(password):
  if re.search(regex_disallowed, password):
    return False
  if not re.search(regex_doubles, password):
    return False
  found_increasing_two = False
  previous_char = '!'
  for char in password:
    if char == chr(ord(previous_char) + 1):
      if found_increasing_two:
        return True
      else:
        found_increasing_two = True
    else:
      found_increasing_two = False
    previous_char = char
  return False

password = previous_password
while password != 'zzzzzzzz':
  password = increment_password(password)
  if valid_password(password):
    print password
    break