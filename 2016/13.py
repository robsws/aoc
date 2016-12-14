#!/usr/local/bin/python
import sys
from copy import deepcopy
from functools import reduce
import time

input_value = int(sys.argv[1])
target = [31, 39]

def is_wall(coord):
  (x, y) = coord
  value = x*x + 3*x + 2*x*y + y + y*y + input_value
  one_bits = 0
  for i in reversed(range(32)):
    bit_value = 2 ** i
    if bit_value > value:
      continue
    else:
      value -= bit_value
      one_bits += 1
  return one_bits % 2 != 0

for x in range(50):
  line = ''
  for y in range(50):
    if is_wall([x,y]):
      line += '#'
    else:
      line += '.'
  print(line)

def score(path):
  # The closer the path to the exit, the better (lower) the score
  return abs(target[0] - path['coord'][0]) + abs(target[1] - path['coord'][1])

def expand_path(path):
  new_paths = []
  # At most three possible paths
  # Check each compass direction
  north = [path['coord'][0], path['coord'][1] + 1]
  south = [path['coord'][0], path['coord'][1] - 1]
  east = [path['coord'][0] + 1, path['coord'][1]]
  west = [path['coord'][0] - 1, path['coord'][1]]
  # North
  if not is_wall(north) and north not in path['visited']:
    new_path = deepcopy(path)
    new_path['coord'] = north
    new_path['length'] += 1
    new_path['visited'] = path['visited'] + [path['coord']]
    new_paths.append(new_path)
  # South
  if not south[1] < 0 and not is_wall(south) and south not in path['visited']:
    new_path = deepcopy(path)
    new_path['coord'] = south
    new_path['length'] += 1
    new_path['visited'] = path['visited'] + [path['coord']]
    new_paths.append(new_path)
  # East
  if not is_wall(east) and east not in path['visited']:
    new_path = deepcopy(path)
    new_path['coord'] = east
    new_path['length'] += 1
    new_path['visited'] = path['visited'] + [path['coord']]
    new_paths.append(new_path)
  # West
  if not west[0] < 0 and not is_wall(west) and west not in path['visited']:
    new_path = deepcopy(path)
    new_path['coord'] = west
    new_path['length'] += 1
    new_path['visited'] = path['visited'] + [path['coord']]
    new_paths.append(new_path)
  return new_paths

paths = [
  {
    'length'   : 0,
    'coord'    : [0,0],
    'visited'  : []
  }
]
finished = False

while not finished:
  # print("****")
  best_path = reduce(lambda p1, p2: p1 if score(p1) < score(p2) else p2, paths)
  # print("Best Path:")
  # print(best_path)
  paths.extend(expand_path(best_path))
  paths.remove(best_path)
  # print("Paths:")
  # print(paths)
  for path in paths:
    if score(path) == 0:
      print(path)
      finished = True
