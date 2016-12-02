#!/usr/local/bin/python
from operator import add

file = open("2_input.txt",'r')
keypad = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
direction_map = {
  'L': [-1, 0],
  'R': [1, 0],
  'D': [0, 1],
  'U': [0, -1]
}

def clamp(n, low_bound, high_bound):
  return max(low_bound, min(n, high_bound))

def move(position, direction):
  position = list(map(add, position, direction_map[direction]))
  position[0] = clamp(position[0], 0, len(keypad[0]) - 1)
  position[1] = clamp(position[1], 0, len(keypad) - 1)
  print(direction+": "+str(position))
  return position

def digit(position):
  return keypad[position[1]][position[0]]

# Main
position = [1,1]
keypad_code = ''
for line in file:
  line = line.rstrip()
  for direction in line:
    position = move(position, direction)
  keypad_code += str(digit(position))
print(keypad_code)
