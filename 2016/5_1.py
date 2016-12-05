#!/usr/local/bin/python
import sys
import hashlib
import re

door_id = sys.argv[1]
password = ''
index = 0
regex = re.compile(r"^00000");
while len(password) < 8:
  door_index = door_id + str(index)
  md5 = hashlib.md5()
  md5.update(door_index)
  digest = md5.hexdigest()
  if re.search(regex, digest):
    password += digest[5]
  index += 1
print(password)