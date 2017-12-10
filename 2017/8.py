#!/usr/local/bin/python
import sys
import re

input_filename = sys.argv[1]
file = open(input_filename,'r')
instruction_regex = re.compile(r"^(\w+) (\w+) (-?\d+) if (\w+) ([!=<>]+) (-?\d+)$")

ops = {
    'inc': lambda x, y: x + y,
    'dec': lambda x, y: x - y
}

bool_ops = {
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y
}

registers = dict()
max_value = 0
for line in file.read().splitlines():
    match = re.search(instruction_regex, line)
    (reg, op, amount, cond_reg, bool_op, cond_amount) = match.groups()
    if reg not in registers:
        registers[reg] = 0
    if cond_reg not in registers:
        registers[cond_reg] = 0
    if bool_ops[bool_op](registers[cond_reg], int(cond_amount)):
        registers[reg] = ops[op](registers[reg], int(amount))
        if registers[reg] > max_value:
            max_value = registers[reg]

print('part 1: '+str(max(registers.values())))
print('part 2: '+str(max_value))