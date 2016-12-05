#!/usr/local/bin/python
import sys
import hashlib
import re
import random

door_id = sys.argv[1]
password_digits = [-1,-1,-1,-1,-1,-1,-1,-1]
index = 0
key_regex = re.compile(r"^00000")
numeric_regex = re.compile(r"^[0-9]$")
# Variables for animation
possible_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

while -1 in password_digits:
  door_index = door_id + str(index)
  md5 = hashlib.md5()
  md5.update(door_index)
  digest = md5.hexdigest()
  if re.search(key_regex, digest) and re.search(numeric_regex, digest[5]) and int(digest[5]) < 8 and password_digits[int(digest[5])] == -1:
    password_digits[int(digest[5])] = digest[6]
  index += 1
  # Animation (only every 10000 iterations to save time)
  if(index % 10000 == 0):
    str_password = ''
    for i in range(8):
      if password_digits[i] == -1:
        str_password += random.choice(possible_digits)
      else:
        str_password += password_digits[i]
    print '\r',
    print str_password,
    sys.stdout.flush()

str_password = reduce(lambda x, y: str(x)+str(y), password_digits)
print '\r',
print str_password,
sys.stdout.flush()
print('ACCESS GRANTED')