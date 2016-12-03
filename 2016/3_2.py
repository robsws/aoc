#!/usr/local/bin/python
import re

file = open("3_input.txt",'r')
regex = re.compile(r"^\s*([^\s]+)\s+([^\s]+)\s+([^\s]+)\s*$");

# Preprocess file to get one long array of numbers
columns = [[],[],[]]
for line in file:
  match = re.search(regex, line)
  (a, b, c) = match.groups()
  columns[0].append(int(a))
  columns[1].append(int(b))
  columns[2].append(int(c))
columns[1].extend(columns[2])
columns[0].extend(columns[1])
number_list = columns[0]

def valid_triangle(a, b, c):
  return a + b > c and b + c > a and c + a > b

valid_triangles = 0
for i in range(0, len(number_list), 3):
  (a, b, c) = number_list[i:i+3]
  valid_triangles += 1 if valid_triangle(a,b,c) else 0
print valid_triangles