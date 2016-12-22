#!/usr/local/bin/python
import sys
file = open(sys.argv[1], 'r')
nodes = [[0 for y in range(27)] for x in range(35)]

for line in file:
  line = line.rstrip()
  (x, y, size, used, avail, percent) = line.split(' ')
  nodes[int(x)][int(y)] = {
    'size'    : int(size),
    'used'    : int(used),
    'avail'   : int(avail),
    'percent' : int(percent)
  }

viable_pairs = 0
for x, column in enumerate(nodes):
  for y, node in enumerate(column):
    if not node['used'] == 0:
      for other_x, other_column in enumerate(nodes):
        for other_y, other_node in enumerate(other_column):
          if not(x == other_x and y == other_y) and node['used'] <= other_node['avail']:
            viable_pairs += 1
print(viable_pairs)