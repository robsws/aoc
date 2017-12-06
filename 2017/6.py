#!/usr/local/bin/python
import sys
import time
from itertools import cycle, dropwhile

input_filename = sys.argv[1]
file = open(input_filename,'r')

lines = list(file.read().splitlines())
blocks = list(map(int, lines[0].split("\t")))
memory = dict()
iterations = 0
blockstr = str(blocks)
while blockstr not in memory:
    memory[blockstr] = iterations
    largest = max(blocks)
    largest_index = blocks.index(largest)
    blocks[largest_index] = 0
    blocks_iterator = dropwhile(lambda x: x[0] < largest_index, cycle(enumerate(blocks)))
    next(blocks_iterator)
    for i, (index, block) in enumerate(blocks_iterator):
        blocks[index] += 1
        if i >= largest - 1:
            break
    blockstr = str(blocks)
    iterations += 1
cycle_length = iterations - memory[blockstr]
print('part1: '+str(iterations))
print('part2: '+str(cycle_length))