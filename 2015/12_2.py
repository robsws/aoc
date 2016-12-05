#!/usr/local/bin/python
import sys
import math
import re

file = open("12_input.txt",'r')

# separate objects out
objects = []
object_parents = {}
object_children = {}
current_object = 0
for line in file:
  for char in line:
    if char == '{':
      objects.append('{')
      prev_object = current_object
      current_object = len(objects) - 1
      object_parents[current_object] = prev_object
      if prev_object not in object_children.keys():
        object_children[prev_object] = [current_object]
      else:
        object_children[prev_object].append(current_object)
    elif char == '}':
      objects[current_object] += '}'
      current_object = object_parents[current_object]
    else:
      objects[current_object] += char

# for num,object in enumerate(objects):
#   print str(num) + ':: '+ str(object)

# check if it has red property and add the numbers if it does not
excluded_children = []
red_regex = re.compile(r':\"red\"')
num_regex = re.compile(r'(-?[0-9]+)')
sum_of_numbers = 0
excluded_sum = 0
for num,object in enumerate(objects):
  if not re.search(red_regex, object) and num not in excluded_children:
    print "including "+str(num)+" "+str(object)
    for match in re.finditer(num_regex, object):
      sum_of_numbers += int(match.group(1))
      print "Adding "+match.group(1)
  else:
    print "excluding "+str(num)+" "+str(object)
    if num in object_children.keys():
      for child in object_children[num]:
        excluded_children.append(child)
        print "marking "+str(child)+" for exclusion"
    for match in re.finditer(num_regex, object):
      # print "Would be adding " + match.group(1)
      excluded_sum += int(match.group(1))

print object_children
print excluded_children 
print sum_of_numbers
print sum_of_numbers + excluded_sum