#!/usr/local/bin/python
import sys
import math

floor = 0
file = open("1_input.txt",'r')

for line in file:
    print "line"
    for char in line:
        if char == '(':
            floor += 1
        if char == ')':
            floor -= 1

print floor
