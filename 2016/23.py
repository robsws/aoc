#!/usr/local/bin/python
import re

registers = {
  'a': 10,
  'b': 0,
  'c': 0,
  'd': 0
}

program = [
  'cpy a b', 
  'dec b',   
  'cpy a d', 
  'cpy 0 a', 
  'cpy b c', 
  'inc a',   
  'dec c',   
  'jnz c -2',
  'dec d',   
  'jnz d -5', 
  'dec b', 
  'cpy b c', 
  'cpy c d', 
  'dec d', 
  'inc c', 
  'jnz d -2', 
  'tgl c',
  'cpy -16 c', 
  'jnz 1 c', 
  'cpy 95 c',
  'jnz 99 d',
  'inc a',
  'inc d',
  'jnz d -2',
  'inc c',
  'jnz c -5'
]

lexical_regex = re.compile(r'[a-z]')
program_counter = 0

def evaluate(a):
  if re.match(lexical_regex, a):
    return registers[a]
  else:
    return int(a)

def cpy(a, b):
  if not re.match(lexical_regex, b):
    return
  a = evaluate(a)
  registers[b] = a

def inc(a):
  if not re.match(lexical_regex, a):
    return
  registers[a] += 1

def dec(a):
  if not re.match(lexical_regex, a):
    return
  registers[a] -= 1 

def jnz(a, b):
  global program_counter
  a = evaluate(a)
  b = evaluate(b)
  if a != 0:
    program_counter += int(b) - 1

def tgl(a):
  global program_counter
  global program
  a = evaluate(a)
  index = program_counter + a
  if index >= len(program):
    return
  code_line = program[index]
  command_parts = code_line.split(' ')
  new_command = ''
  if len(command_parts) == 2:
    (command, a) = command_parts
    if command == 'inc':
      new_command = 'dec'
    else:
      new_command = 'inc'
  else:
    (command, a, b) = command_parts
    if command == 'jnz':
      new_command = 'cpy'
    else:
      new_command = 'jnz'
  program[index] = " ".join([new_command] + command_parts[1:])
  print(registers)


commands = {
  'cpy': cpy,
  'inc': inc,
  'dec': dec,
  'jnz': jnz,
  'tgl': tgl
}

while program_counter < len(program):
  b = None
  command_parts = program[program_counter].split(' ')
  if program_counter >= 18:
    print(registers)
    print(command_parts)
  if len(command_parts) == 2:
    (command, a) = command_parts
    commands[command](a)
  else:
    (command, a, b) = command_parts
    commands[command](a,b)
  program_counter += 1

print(registers)