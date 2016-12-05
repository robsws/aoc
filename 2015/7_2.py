#!/usr/local/bin/python
import sys
import math
import re

file = open("7_input.txt",'r')

circuit = {}
# contains nodes like this
# key: ID of wire
# value: how to calculate signal on wire

# x => {value: 123}
# y => {value: 456}
# d => {op: AND, input1: x, input2: y}
# e => {op: OR, input1: x, input2: y}
# f => {op: LSHIFT, input: x, shift_value: 2}
# g => {op: RSHIFT, input: y, shift_value: 2}
# h => {op: NOT, input: x}
# i => {op: NOT, input: y}

print "Parsing instructions..."
for line in file:
  # parse the line
  regex = re.compile(r'^(?:([0-9]+|[a-z]+)|(?:NOT ([0-9]+|[a-z]+))|([0-9]+|[a-z]+) (?:AND ([0-9]+|[a-z]+)|OR ([0-9]+|[a-z]+)|LSHIFT ([0-9]+)|RSHIFT ([0-9]+))) -> ([a-z]+)$')

  # set up the circuit by adding entries to the circuit dict
  match = re.search(regex, line)
  if match:
    # assign all the captured groups in the regex to variables
    (
      assign_value, # number/ID for assignment
      not_input,  # wire where left side is a NOT expression
      binary_op_left_input, # wire on left side of binary operation
      and_right_input, # wire on right side of AND operation
      or_right_input, # wire on right side of OR operation
      lshift_value, # number on right side of LSHIFT operation
      rshift_value, # number on right side of RSHIFT operation
      output # output wire
    ) = match.groups()

    # figure out what we should add to the circuit
    if assign_value: # assignment operation
      circuit[output] = {
        'op': 'ASSIGN',
        'input': assign_value,
      }
    elif not_input: # not gate
      circuit[output] = {
        'op': 'NOT',
        'input': not_input,
      }
    elif and_right_input: # and operation
      circuit[output] = {
        'op': 'AND',
        'input1': binary_op_left_input,
        'input2': and_right_input,
      }
    elif or_right_input: # or operation
      circuit[output] = {
        'op': 'OR',
        'input1': binary_op_left_input,
        'input2': or_right_input,
      }
    elif lshift_value: # lshift operation
      circuit[output] = {
        'op': 'LSHIFT',
        'input': binary_op_left_input,
        'shift_value': int(lshift_value),
      }
    elif rshift_value: # rshift operation
      circuit[output] = {
        'op': 'RSHIFT',
        'input': binary_op_left_input,
        'shift_value': int(rshift_value),
      }

# OVERRIDE INPUT B
circuit['b'] = {
  'op': 'ASSIGN',
  'input': '16076'
}

# Helper function definitions for running the circuit
def is_numeric(string):
  # Test if a string is numeric
  try:
    int(string)
    return True
  except ValueError:
    return False

def get_value(input):
  # Find a signal value from a string (either an integer or a wire ID)
  if is_numeric(input):
    return int(input)
  else:
    return int(signal(input))

def signal(wire):
  # Calculate the signal on a particular wire recursively
  if not wire in circuit.keys():
    print "No input on wire "+wire
    return 0 # null signal if nothing is providing input
  if not 'value' in circuit[wire].keys():
    # we haven't already calculated a signal for this wire
    # each value is passed through a 16 bit mask
    if circuit[wire]['op'] == 'ASSIGN': # assign operation
      circuit[wire]['value'] = 0xffff & get_value(circuit[wire]['input'])
    elif circuit[wire]['op'] == 'NOT': # not gate
      circuit[wire]['value'] = 0xffff & ~get_value(circuit[wire]['input'])
    elif circuit[wire]['op'] == 'AND': # and gate
      circuit[wire]['value'] = 0xffff & (get_value(circuit[wire]['input1']) & get_value(circuit[wire]['input2']))
    elif circuit[wire]['op'] == 'OR': # or gate
      circuit[wire]['value'] = 0xffff & (get_value(circuit[wire]['input1']) | get_value(circuit[wire]['input2']))
    elif circuit[wire]['op'] == 'LSHIFT': # lshift gate
      circuit[wire]['value'] = 0xffff & (get_value(circuit[wire]['input']) << int(circuit[wire]['shift_value']))
    elif circuit[wire]['op'] == 'RSHIFT': # rshift gate
      circuit[wire]['value'] = 0xffff & (get_value(circuit[wire]['input']) >> int(circuit[wire]['shift_value']))
  return circuit[wire]['value']

print "Emulating circuit..."
# Run the circuit by recursively calculating the signal for each wire
for wire in circuit.keys():
  signal(wire)

# for keys,values in circuit.items():
#     print(keys)
#     print(values)

print "Value on wire a: "+str(circuit["a"]["value"])