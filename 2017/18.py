import sys
import re
import winsound
import time

input_filename = sys.argv[1]
file = open(input_filename,'r')
lines = file.read().splitlines()
program_regex = re.compile(r'^(\w+) ([-\w]+)(?: ([-\w]+))?$')
listing = []

for line in lines:
    match = re.search(program_regex, line)
    listing.append(tuple(match.groups()))

registers = {}
last_frequency = 0
program_counter = 0
recovered_frequency = 0

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

def play_sound(x):
    global last_frequency
    val = evaluate(x)
    last_frequency = val
    # winsound.Beep(val, 400)
    increment_program_counter()

def set_register(register, x):
    init_register(register)
    registers[register] = evaluate(x)
    increment_program_counter()

def incr_register(register, x):
    init_register(register)
    registers[register] += evaluate(x)
    increment_program_counter()    

def multiply_register(register, x):
    init_register(register)
    registers[register] *= evaluate(x)
    increment_program_counter()    

def modulo_register(register, x):
    init_register(register)
    registers[register] = registers[register] % evaluate(x)
    increment_program_counter()    

def recover_last_frequency(x):
    if evaluate(x) != 0:
        recovered_frequency = last_frequency
        print("part 1: "+str(recovered_frequency))
        exit(1)
    increment_program_counter()    

def jump_if_greater_than(x, y):
    if evaluate(x) > 0:
        global program_counter
        program_counter += evaluate(y)
    else:
        increment_program_counter()

instructions = {
    'snd': play_sound,
    'set': set_register,
    'add': incr_register,
    'mul': multiply_register,
    'mod': modulo_register,
    'rcv': recover_last_frequency,
    'jgz': jump_if_greater_than
}

while program_counter < len(listing):
    # print(program_counter)    
    # print(listing[program_counter])
    operation = listing[program_counter]
    if operation[2] == None:
        instructions[operation[0]](operation[1])
    else:
        instructions[operation[0]](operation[1],operation[2])
    # print(registers)  