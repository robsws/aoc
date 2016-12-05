#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

file = open(argv[1],'r')

# Parsing
grid = []
for i,line in enumerate(file):
  grid.append([])
  for char in line:
    if char == '#':
      grid[i].append(1)
    else:
      grid[i].append(0)

def printGrid():
  for x in range(100):
    line = ''
    for y in range(100):
      if grid[x][y] == 1:
        line += '#'
      else:
        line += '.'
    print line

# Iterate through Conway cycles
for i in range(100):
  next_grid = copy.deepcopy(grid)
  for x in range(100):
    for y in range(100):
      cell_fitness = 0
      for neighbour_x in range(x-1, x+2):
        if neighbour_x < 0 or neighbour_x > 99:
          continue
        for neighbour_y in range(y-1, y+2):
          if neighbour_y < 0 or neighbour_y > 99:
            continue
          if neighbour_x == x and neighbour_y == y:
            continue
          cell_fitness += grid[neighbour_x][neighbour_y]
      if grid[x][y] == 1: # Alive!
        # If two or three neighbours are alive I stay alive
        if cell_fitness < 2 or cell_fitness > 3:
          next_grid[x][y] = 0
      else: # Dead :(
        # If three neighbours are alive, I resurrect!
        if cell_fitness == 3:
          next_grid[x][y] = 1
  # Force the corners to be always on
  next_grid[0][0] = 1
  next_grid[0][99] = 1
  next_grid[99][0] = 1
  next_grid[99][99] = 1
  grid = next_grid
  printGrid()

# Count number of alive cells
total = 0
for x in range(100):
  for y in range(100):
    total += grid[x][y]
print total
