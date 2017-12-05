#!/usr/local/bin/python
import sys

part = int(sys.argv[1])
input_filename = sys.argv[2]
file = open(input_filename,'r')

instructions = list(map(int, file.read().splitlines()))
pc = 0
steps = 0
while pc >= 0 and pc < len(instructions):
    oldpc = pc
    pc += instructions[pc]
    if part == 1 or instructions[oldpc] < 3:    
        instructions[oldpc] += 1
    else:
        instructions[oldpc] -= 1

    steps += 1
print(pc)
print(steps)