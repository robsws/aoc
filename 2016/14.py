#!/usr/local/bin/python
import sys
import hashlib
import re
import time

repeat3_regex = re.compile(r'000|111|222|333|444|555|666|777|888|999|aaa|bbb|ccc|ddd|eee|fff')
repeat5_regex = re.compile(r'00000|11111|22222|33333|44444|55555|66666|77777|88888|99999|aaaaa|bbbbb|ccccc|ddddd|eeeee|fffff')

salt = sys.argv[1]

keys = []
pending_keys = []
index = 0

while len(keys) < 64:

  plaintext = salt+str(index)
  ciphertext = hashlib.md5(plaintext.encode('utf-8')).hexdigest()

  # Update counters
  for key in pending_keys:
    key['count'] += 1
    if key['count'] > 1000:
      pending_keys.remove(key)

  # Find strings of 5 same characters
  matches = re.findall(repeat5_regex, ciphertext)
  if len(matches) > 0:
    for match in matches:
      chain = match
      for key in pending_keys:
        if key['char'] == chain[0]:
          keys.append(key)
          pending_keys.remove(key)

  # Find strings of 3 same characters
  match = re.search(repeat3_regex, ciphertext)
  if match:
    chain = match.group(0)
    key = {
      'index'     : index,
      'char'      : chain[0],
      'count'     : 0
    }
    pending_keys.append(key)
  index += 1

# sorted_keys = sorted(keys, key=lambda k: k['index'])
# for i, key in enumerate(keys):
#   print(i)
#   print(key)
# print("****")
# print(sorted_keys[63])