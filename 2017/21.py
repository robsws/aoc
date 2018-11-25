import sys
import re
import time
from math import sqrt

input_filename = sys.argv[1]
iterations = int(sys.argv[2])
file = open(input_filename,'r')
lines = file.read().splitlines()

def flip_horizontal(grid):
    flipped = list()
    for row in grid:
        flipped.append(tuple(reversed(row)))
    return tuple(flipped)

def flip_vertical(grid):
    return tuple(reversed(grid))

def rotate_90(grid):
    if len(grid) == 2:
        row1 = (grid[1][0], grid[0][0])
        row2 = (grid[1][1], grid[0][1])
        return (row1, row2)
    else:
        row1 = (grid[2][0], grid[1][0], grid[0][0])
        row2 = (grid[2][1], grid[1][1], grid[0][1])
        row3 = (grid[2][2], grid[1][2], grid[0][2])
        return (row1, row2, row3)


two_rule_regex = re.compile(r'^([\.#]+)\/([\.#]+) => ([\.#\/]+)\/([\.#]+)\/([\.#]+)$')
three_rule_regex = re.compile(r'^([\.#]+)\/([\.#]+)\/([\.#]+) => ([\.#\/]+)\/([\.#]+)\/([\.#]+)\/([\.#]+)$')

# figure out all of the expansion rules, taking
# transformations into account
expansion_rules = dict()
for line in lines:
    match = re.search(two_rule_regex, line)
    lvalue = tuple()
    rvalue = tuple()
    if match:
        (lrow1, lrow2, rrow1, rrow2, rrow3) = match.groups()
        lvalue = (tuple(lrow1),tuple(lrow2))
        rvalue = (tuple(rrow1),tuple(rrow2),tuple(rrow3))
        expansion_rules[lvalue] = rvalue
    else:
        match = re.search(three_rule_regex, line)
        if match:
            (lrow1, lrow2, lrow3, rrow1, rrow2, rrow3, rrow4) = match.groups()
            lvalue = (tuple(lrow1),tuple(lrow2),tuple(lrow3))
            rvalue = (tuple(rrow1),tuple(rrow2),tuple(rrow3),tuple(rrow4))
    expansion_rules[lvalue] = rvalue
    expansion_rules[flip_horizontal(lvalue)] = rvalue
    expansion_rules[flip_vertical(lvalue)] = rvalue
    expansion_rules[flip_horizontal(flip_vertical(lvalue))] = rvalue
    rot1 = rotate_90(lvalue)
    expansion_rules[rot1] = rvalue
    expansion_rules[flip_horizontal(rot1)] = rvalue
    expansion_rules[flip_vertical(rot1)] = rvalue
    expansion_rules[flip_horizontal(flip_vertical(rot1))] = rvalue
    rot2 = rotate_90(rot1)
    expansion_rules[rot2] = rvalue
    expansion_rules[flip_horizontal(rot2)] = rvalue
    expansion_rules[flip_vertical(rot2)] = rvalue
    expansion_rules[flip_horizontal(flip_vertical(rot2))] = rvalue
    rot3 = rotate_90(rot2)
    expansion_rules[rot3] = rvalue
    expansion_rules[flip_horizontal(rot3)] = rvalue
    expansion_rules[flip_vertical(rot3)] = rvalue
    expansion_rules[flip_horizontal(flip_vertical(rot3))] = rvalue

# define expansion functions
def split_four(pattern):
    split_patterns = []
    split_patterns.append((tuple(pattern[0][0:2]),tuple(pattern[1][0:2])))
    split_patterns.append((tuple(pattern[0][2:4]),tuple(pattern[1][2:4])))
    split_patterns.append((tuple(pattern[2][0:2]),tuple(pattern[3][0:2])))
    split_patterns.append((tuple(pattern[2][2:4]),tuple(pattern[3][2:4])))
    return split_patterns

def join_patterns(patterns):
    joined_grid = []
    width = int(sqrt(len(patterns)))
    for i in range(width): # for each row of patterns
        for j in range(len(patterns[0])): # for each row line
            joined_row = [k for t in map(lambda x: x[j], patterns[i*width : i*width + width]) for k in t]
            joined_grid.append(tuple(joined_row))
    return tuple(joined_grid)

def split_grid(joined_grid):
    split_grid = []
    split_num = 2
    if len(joined_grid)%2 == 0:
        split_num = 2
    elif len(joined_grid)%3 == 0:
        split_num = 3
    else:
        print("there's a problem")
    print(len(joined_grid), split_num)
    split_rows = []
    for row in joined_grid:
        split_rows.append(tuple([row[i:i+split_num] for i in range(0, len(row), split_num)]))
    for col in range(len(split_rows[0])):
        for bigrow in range(len(split_rows[0])):
            pattern = []
            for row in range(split_num):
                pattern.append(split_rows[bigrow*split_num + row][col])
            split_grid.append(tuple(pattern))
    return tuple(split_grid)

def expand(patterns):
    next_patterns = []
    for pattern in patterns:
        next_pattern = expansion_rules[pattern]
        next_patterns.append(next_pattern)
    joined_grid = join_patterns(next_patterns)
    return split_grid(joined_grid)

def get_amount_on(patterns):
    amount_on = 0
    for pattern in patterns:
        for row in pattern:
            for pixel in row:
                if pixel == '#':
                    amount_on += 1
    return amount_on

# start the expansion process
first_row1 = tuple('.#.')
first_row2 = tuple('..#')
first_row3 = tuple('###')
patterns = [(first_row1, first_row2, first_row3)]
for i in range(iterations):
    print("iter", i+1)
    patterns = expand(patterns)
    print(get_amount_on(patterns))

# count number of pixels are on
print(patterns)
print(get_amount_on(patterns))