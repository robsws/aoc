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
finished = False
while not finished:
  finished = True
  for r in ranges:
    if i >= r[0] and i <= r[1]:
      i = r[1] + 1
      finished = False
      break
  amount += 1
print(i)
