#!/usr/local/bin/python
import re

registers = {
  'a': 0,
  'b': 0,
  'c': 1,
  'd': 0
}

program = [
  'cpy 1 a',
  'cpy 1 b',
  'cpy 26 d',
  'jnz c 2',
  'jnz 1 5',
  'cpy 7 c',
  'inc d',
  'dec c',
  'jnz c -2',
  'cpy a c',
  'inc a',
  'dec b',
  'jnz b -2',
  'cpy c b',
  'dec d',
  'jnz d -6',
  'cpy 18 c',
  'cpy 11 d',
  'inc a',
  'dec d',
  'jnz d -2',
  'dec c',
  'jnz c -5'
]

program_counter = 0

def evaluate(expr):
  if re.match(r'[a-z]',a):
    return registers[a]
  else:
    return int(a)

def cpy(a, b):
  a = evaluate(a)
  registers[b] = a

def inc(a):
  registers[a] += 1

def dec(a):
  registers[a] -= 1 

def jnz(a, b):
  global program_counter
  a = evaluate(a)
  if a != 0:
    program_counter += int(b) - 1

commands = {
  'cpy': cpy,
  'inc': inc,
  'dec': dec,
  'jnz': jnz
}

while program_counter < len(program):
  b = None
  command_parts = program[program_counter].split(' ')
  if len(command_parts) == 2:
    (command, a) = command_parts
    commands[command](a)
  else:
    (command, a, b) = command_parts
    commands[command](a,b)
  program_counter += 1

print(registers)

