import sys
import re
import time

input_filename = sys.argv[1]
file = open(input_filename,'r')
lines = file.read().splitlines()
program_regex = re.compile(r'^(\w+) ([-\w]+)(?: ([-\w]+))?$')
listing = []

for line in lines:
    match = re.search(program_regex, line)
    listing.append(tuple(match.groups()))

registers = {
    'a': 1,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
}
program_counter = 0

numeric_regex = re.compile(r'^[-\d]+$')

def init_register(x):
    if x not in registers:
        registers[x] = 0

def increment_program_counter():
    global program_counter
    program_counter += 1

def evaluate(x):
    if numeric_regex.match(x):
        return int(x)
    init_register(x)
    return registers[x]

def set_register(register, x):
    init_register(register)
    registers[register] = evaluate(x)
    increment_program_counter()

def sub_register(register, x):
    init_register(register)
    registers[register] -= evaluate(x)
    increment_program_counter()    

times_multiplied = 0
def multiply_register(register, x):
    global times_multiplied
    times_multiplied += 1
    init_register(register)
    registers[register] *= evaluate(x)
    increment_program_counter()    

def jump_if_not_zero(x, y):
    if evaluate(x) != 0:
        global program_counter
        program_counter += evaluate(y)
    else:
        increment_program_counter()

instructions = {
    'set': set_register,
    'sub': sub_register,
    'mul': multiply_register,
    'jnz': jump_if_not_zero
}

i = 0
h = -1
while program_counter < len(listing):
    # print(program_counter)    
    # print(listing[program_counter])
    operation = listing[program_counter]
    if operation[2] == None:
        instructions[operation[0]](operation[1])
    else:
        instructions[operation[0]](operation[1],operation[2])
    print(i, registers)
    if h != registers['h']:
        print(registers['h'])
        h = registers['h']
    i += 1

print(times_multiplied)
print(registers)