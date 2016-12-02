#!/usr/local/bin/python
from operator import add

file = open("2_input.txt",'r')
keypad = [
  ['-', '-', '1', '-', '-'],
  ['-', '2', '3', '4', '-'],
  ['5', '6', '7', '8', '9'],
  ['-', 'A', 'B', 'C', '-'],
  ['-', '-', 'D', '-', '-']
]
direction_map = {
  'L': [-1, 0],
  'R': [1, 0],
  'D': [0, 1],
  'U': [0, -1]
}

def clamp(n, low_bound, high_bound):
  return max(low_bound, min(n, high_bound))

def digit(position):
  return keypad[position[1]][position[0]]

def move(position, direction):
  new_position = list(map(add, position, direction_map[direction]))
  new_position[0] = clamp(new_position[0], 0, len(keypad[0]) - 1)
  new_position[1] = clamp(new_position[1], 0, len(keypad) - 1)
  if digit(new_position) == '-':
    new_position = position
  return new_position

# Main
position = [1,1]
keypad_code = ''
for line in file:
  line = line.rstrip()
  for direction in line:
    position = move(position, direction)
  keypad_code += str(digit(position))
print(keypad_code)
