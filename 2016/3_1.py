#!/usr/local/bin/python
import re

file = open("3_input.txt",'r')
regex = re.compile(r"^\s*([^\s]+)\s+([^\s]+)\s+([^\s]+)\s*$");

def valid_triangle(a, b, c):
  return a + b > c and b + c > a and c + a > b

valid_triangles = 0
for line in file:
  match = re.search(regex, line)
  (a, b, c) = match.groups()
  valid_triangles += 1 if valid_triangle(int(a), int(b), int(c)) else 0
print valid_triangles