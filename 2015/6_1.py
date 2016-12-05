#!/usr/local/bin/python
import sys
import math
import re

file = open("6_input.txt",'r')
grid = [[0 for i in range(1000)] for j in range(1000)]

def turn_on(x, y):
  grid[x][y] = 1

def turn_off(x, y):
  grid[x][y] = 0

def toggle(x, y):
  if grid[x][y] == 1:
    grid[x][y] = 0
  else:
    grid[x][y] = 1

actions = {
  "turn on": turn_on,
  "turn off": turn_off,
  "toggle": toggle,
}

for line in file:
  # parse the line
  regex = re.compile(r'(turn on|turn off|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)')
  match = re.search(regex, line)
  if match:
    action = actions[match.group(1)]
    start_x = int(match.group(2))
    start_y = int(match.group(3))
    end_x = int(match.group(4))
    end_y = int(match.group(5))
    # loop through the grid performing the action given
    for x in range(start_x, end_x + 1):
      for y in range(start_y, end_y + 1):
        action(x,y)

# count the number of lights switched on
total_turned_on = 0
for x in range(1000):
  print ' '
  for y in range(1000):
    if grid[x][y] == 1:
      print '.',
    else:
      print 'x',
    total_turned_on += grid[x][y]
print ' '
print "Total lights turned on: "+str(total_turned_on)