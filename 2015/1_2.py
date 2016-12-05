#!/usr/local/bin/python
import sys
import math

floor = 0
file = open("1_input.txt",'r')
hitbasement = False

for line in file:
    for pos,char in enumerate(line):
        if char == '(':
            floor += 1
        if char == ')':
            floor -= 1
        if floor < 0 and not hitbasement:
            print "in the basement at position "+str(pos+1)+"!"
            hitbasement = True
        
print "final floor: "+str(floor)
