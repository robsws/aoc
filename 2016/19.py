#!/usr/local/bin/python
import sys
no_of_elves = int(sys.argv[1])
elves = range(0, no_of_elves)
i = -1
removed_elves = set()
while len(removed_elves) < no_of_elves - 1:
  for j in range(2):
    i = (i + 1) % no_of_elves
    while(i in removed_elves):
      i = (i + 1) % no_of_elves
  removed_elves.add(i)
remaining = [item for item in elves if item not in removed_elves]
print(remaining[0] + 1)