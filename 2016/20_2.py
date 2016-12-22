#!/usr/local/bin/python
import sys
file = open(sys.argv[1], 'r')

ranges = []
for line in file:
  line = line.rstrip()
  (low, high) = line.split('-')
  (low, high) = (int(low), int(high))
  ranges.append([low,high])
# sort by highest
ranges = sorted(ranges, key=lambda x: x[1])

i = 0
amount = 0
while i <= 4294967295:
  found = False
  for r in ranges:
    if i >= r[0] and i <= r[1]:
      i = r[1] + 1
      found = True
      break
  if not found:
    i += 1
    amount += 1
print(amount)
