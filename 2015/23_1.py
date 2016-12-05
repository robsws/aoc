#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

file = open('23_input.txt', 'r')

regex = re.compile(r'(hlf|tpl|inc|jmp|jie|jio) ([ab]|(?:\+|\-)[0-9]+)(?:, ((?:\+|\-)[0-9]+))?')
instructions = []

for line in file:
  match = re.search(regex, line)
  if not match:
    raise Exception("no match")
  instruction = {}
  (ins, arg, arg2) = match.groups()
  instruction["ins"] = ins
  instruction["arg"] = arg
  instruction["arg2"] = arg2
  instructions.append(instruction)

registers = {"a":1, "b":0}
idx = 0
while idx >= 0 and idx < len(instructions):
  print idx
  print instructions[idx]
  print registers
  ins = instructions[idx]
  if ins["ins"] == "hlf":
    # half value of register
    registers[ins["arg"]] = int(math.floor(registers[ins["arg"]] / 2.0))
    idx += 1
  elif ins["ins"] == "tpl":
    # triple value of register
    registers[ins["arg"]] *= 3
    idx += 1
  elif ins["ins"] == "inc":
    # increment register
    registers[ins["arg"]] += 1
    idx += 1
  elif ins["ins"] == "jmp":
    idx += int(ins["arg"])
  elif ins["ins"] == "jie":
    if registers[ins["arg"]] % 2 == 0:
      idx += int(ins["arg2"])
    else:
      idx += 1
  elif ins["ins"] == "jio":
    if registers[ins["arg"]] == 1:
      idx += int(ins["arg2"])
    else:
      idx += 1

print registers