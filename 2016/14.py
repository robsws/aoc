#!/usr/local/bin/python
import sys
import hashlib
import re
import time

repeat3_regex = re.compile(r'000|111|222|333|444|555|666|777|888|999|aaa|bbb|ccc|ddd|eee|fff')
repeat5_regex = re.compile(r'00000|11111|22222|33333|44444|55555|66666|77777|88888|99999|aaaaa|bbbbb|ccccc|ddddd|eeeee|fffff')

part = sys.argv[1]
salt = sys.argv[2]

keys = []
pending_keys = []
index = 0

while len(keys) < 100:

  plaintext = salt+str(index)
  hashtext = plaintext
  number_of_hashes = 2017 if part == '2' else 1
  for i in range(number_of_hashes):
    hashtext = hashlib.md5(hashtext.encode('utf-8')).hexdigest()

  # Update counters
  keys_to_remove = []
  for key in pending_keys:
    key['count'] += 1
    if key['count'] > 1000:
      keys_to_remove.append(key)
  for key in keys_to_remove:
    pending_keys.remove(key)

  # Find strings of 5 same characters
  matches = re.findall(repeat5_regex, hashtext)
  if len(matches) > 0:
    for match in matches:
      chain = match
      keys_to_remove = []
      for key in pending_keys:
        if key['char'] == chain[0]:
          keys.append(key)
          keys_to_remove.append(key)
      for key in keys_to_remove:
        pending_keys.remove(key)

  # Find strings of 3 same characters
  match = re.search(repeat3_regex, hashtext)
  if match:
    chain = match.group(0)
    key = {
      'index'     : index,
      'char'      : chain[0],
      'count'     : 0
    }
    pending_keys.append(key)
  index += 1

sorted_keys = sorted(keys, key=lambda k: k['index'])
for i, key in enumerate(sorted_keys):
  print(i)
  print(key)
print("****")
print(sorted_keys[63])