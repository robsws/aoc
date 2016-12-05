#!/usr/local/bin/python
import sys
import math

total_area = 0
file = open("2_input.txt",'r')

for line in file:
  dimensions = line.split('x')
  length = int(dimensions[0]) #length
  width = int(dimensions[1]) #width
  height = int(dimensions[2]) #height

  # calculate surface area
  face_areas = [length * width, width * height, height * length];
  surface_area = 2*face_areas[0] + 2*face_areas[1] + 2*face_areas[2]

  # calculate extra paper
  extra_paper = min(face_areas)

  # add to total
  total_area += surface_area + extra_paper

print "Amount of paper needed: "+str(total_area)