#!/usr/local/bin/python
import sys
import math

total_area = 0
total_ribbon = 0
file = open("2_input.txt",'r')

for line in file:
  dimensions = line.split('x')
  length = int(dimensions[0]) #length
  width = int(dimensions[1]) #width
  height = int(dimensions[2]) #height

  # calculate smallest perimeter for ribbon
  dimensions = [length, width, height]
  smallest_length = dimensions.pop(dimensions.index(min(dimensions)))
  smallest_width = dimensions.pop(dimensions.index(min(dimensions)))
  perimeter = smallest_length*2 + smallest_width*2

  # calculate extra ribbon
  extra_ribbon = length * width * height

  # calculate surface area
  face_areas = [length * width, width * height, height * length];
  surface_area = 2*face_areas[0] + 2*face_areas[1] + 2*face_areas[2]

  # calculate extra paper
  extra_paper = min(face_areas)

  # add to totals
  total_area += surface_area + extra_paper
  total_ribbon += perimeter + extra_ribbon

print "Amount of paper needed: "+str(total_area)
print "Amount of ribbon needed: "+str(total_ribbon)