#!/usr/local/bin/python
import sys
from collections import defaultdict

part = int(sys.argv[1])
input_val = int(sys.argv[2])

grid = defaultdict(dict)
grid[0][0] = 1
def calculate_grid_value(current_x, current_y):
    grid[current_x][current_y] = 0
    for x in range(current_x - 1, current_x + 2):
        for y in range(current_y - 1, current_y + 2):
            if y in grid.get(x, {}) and not (current_x == x and current_y == y):
                grid[current_x][current_y] += grid[x][y]
    print(str(current_x) + ", " + str(current_y))
    print(grid[current_x][current_y])
    return grid[current_x][current_y]

value = 1
current_x = 1
current_y = 0
moves_before_turning = 2
while value < input_val:
    for i in range(moves_before_turning - 1):
        value = calculate_grid_value(current_x, current_y)
        current_y -= 1
    for i in range(moves_before_turning):
        value = calculate_grid_value(current_x, current_y)
        current_x -= 1
    for i in range(moves_before_turning):
        value = calculate_grid_value(current_x, current_y)
        current_y += 1
    for i in range(moves_before_turning + 1):
        value = calculate_grid_value(current_x, current_y)
        current_x += 1
    moves_before_turning += 2