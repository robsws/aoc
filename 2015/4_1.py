#!/usr/local/bin/python
import sys
import math
import md5
import re


secret = sys.argv[1]
key_number = 1
while True:
  key = secret + str(key_number)
  digest = md5.new(key).hexdigest()
  if re.search("^00000", digest):
    print "Key: "+key+" Digest: "+digest
    break
  key_number += 1
