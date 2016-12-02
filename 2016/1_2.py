#!/usr/local/bin/python
import sys
import math
import re
from operator import add

file = open("1_input.txt",'r')
regex = re.compile(r"([LR])(\d+)");

turn_map = {
  'L': -1,
  'R': 1
}

direction_map = {
  0: [0,1],
  1: [1,0],
  2: [0,-1],
  3: [-1,0]
}

current_position = [0,0]
current_direction = 0 # 0-N 1-E 2-S 3-W
positions_visited = {"0,0": 1}

def done(strposition, positions_visited, current_position):
  if strposition in positions_visited:
    print(str(abs(current_position[0]) + abs(current_position[1])))
    return 1
  else:
    return 0

def turn(direction, current_direction):
  current_direction += turn_map[direction]
  if current_direction > 3:
    current_direction = 0
  elif current_direction < 0:
    current_direction = 3
  return current_direction

def move(distance, current_direction, current_position, positions_visited):
  for i in range(1, distance+1):
    current_position = list(map(add, current_position, direction_map[current_direction]))
    strposition = str(current_position[0])+","+str(current_position[1])
    if done(strposition, positions_visited, current_position):
      sys.exit()
    else:
      positions_visited[strposition] = 1
  return current_position

for line in file:
  instructions = line.split(',')
  for instruction in instructions:
    match = re.search(regex, instruction)
    (direction, distance) = match.groups()
    current_direction = turn(direction, current_direction)
    current_position = move(int(distance), current_direction, current_position, positions_visited)
    strposition = str(current_position[0])+","+str(current_position[1])
    

