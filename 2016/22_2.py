#!/usr/local/bin/python
import sys
from copy import deepcopy
from functools import reduce
import hashlib
import json

file = open(sys.argv[1], 'r')
start_state = {'moves': 0, 'goal':[int(sys.argv[2]),0], 'visited_hashes':set()}
start_state['nodes'] = [[0 for y in range(int(sys.argv[3]))] for x in range(int(sys.argv[2]))]

for line in file:
  line = line.rstrip()
  (x, y, size, used, avail, percent) = line.split(' ')
  start_state['nodes'][int(x)][int(y)] = {
    'size'    : int(size),
    'used'    : int(used),
    'avail'   : int(avail),
    'goal'    : False
  }

start_state['nodes'][int(sys.argv[3])-1][0]['goal'] = True

def hash_state(state):
  serialised = json.dumps(state['nodes'], sort_keys=True) + json.dumps(state['goal'])
  return hashlib.md5(serialised).hexdigest()

# Lower score = better
def score(state):
  # work out how far the goal is from 0,0
  goal_distance = state['goal'][0] + state['goal'][1]
  # work out how far away the nearest empty node is
  empty_node_score = 0
  for x, column in enumerate(state['nodes']):
    for y, node in enumerate(column):
      node_dist = abs(x - state['goal'][0] - 1) + abs(y - state['goal'][1])
      if node['used'] == 0:
        empty_node_score += node_dist
  return goal_distance * 10000000 + empty_node_score * 1000 + state['moves']

def create_next_state(state, from_x, from_y, to_x, to_y):
  from_node = state['nodes'][from_x][from_y]
  to_node = state['nodes'][to_x][to_y]
  next_state = deepcopy(state)
  next_state['moves'] += 1
  next_state['nodes'][from_x][from_y]['avail'] = from_node['size']
  next_state['nodes'][from_x][from_y]['used'] = 0
  next_state['nodes'][to_x][to_y]['avail'] = to_node['avail'] - from_node['used']
  next_state['nodes'][to_x][to_y]['used'] = to_node['used'] + from_node['used']
  if from_node['goal']:
    next_state['nodes'][from_x][from_y]['goal'] = False
    next_state['nodes'][to_x][to_y]['goal'] = True
    next_state['goal'] = [to_x, to_y]
  hashed_state = hash_state(next_state)
  if hashed_state in state['visited_hashes']:
    return {'invalid':1}
  else:
    next_state['visited_hashes'].add(hashed_state)
    return next_state

def get_next_states(state):
  states = []
  nodes = state['nodes']
  # look at all possible moves
  for x, column in enumerate(nodes):
    for y, node in enumerate(column):
      if not node['used'] == 0:
        # look in compass directions
        # left
        if x > 0 and nodes[x-1][y]['avail'] > node['used']:
          next_state = create_next_state(state, x, y, x-1, y)
          if 'invalid' not in next_state:
            states.append(next_state)
        # up
        if y > 0 and nodes[x][y-1]['avail'] > node['used']:
          next_state = create_next_state(state, x, y, x, y-1)
          if 'invalid' not in next_state:
            states.append(next_state)
        # right
        if x < len(nodes) - 1 and nodes[x+1][y]['avail'] > node['used']:
          next_state = create_next_state(state, x, y, x+1, y)
          if 'invalid' not in next_state:
            states.append(next_state)
        # down
        if y < len(nodes[0]) - 1 and nodes[x][y+1]['avail'] > node['used']:
          next_state = create_next_state(state, x, y, x, y+1)
          if 'invalid' not in next_state:
            states.append(next_state)
  return states

possible_states = [start_state]
best_state_score = 1000000000
finished = False

while not finished:
  best_state = reduce(lambda p1, p2: p1 if score(p1) < score(p2) else p2, possible_states)
  print len(possible_states)
  best_state_score = score(best_state)
  print(best_state_score)
  if best_state_score < 100000:
    finished = True
    print(best_state['moves'])
  else:
    next_states = get_next_states(best_state)
    possible_states.extend(next_states)
    possible_states.remove(best_state)

