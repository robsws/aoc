#!/usr/local/bin/python
file = open("6_input.txt",'r')
import time

positions = []
for line in file:
  line = line.rstrip()
  if not positions:
    for i in range(len(line)):
      positions.append([])
  for i,char in enumerate(line):
    positions[i].append(char)

def anti_mode(char_list):
  char_count = {}
  for char in char_list:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  return reduce(lambda x,y: x if char_count[x] < char_count[y] else y, char_list)

message = ''
for position in positions:
  message += anti_mode(position)
print(message)