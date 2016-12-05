#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy
from operator import mul

file = open('24_input.txt', 'r')

# Three groups of packages
# All the same weight
# Smallest amount possible in the passenger section
# Passenger section config with the smallest QE
# QE = product(weights)

packages = []
total_weight = 0
for line in file:
  packages.append(int(line))
  total_weight += int(line)

group_weight = total_weight/4
packages.sort(reverse=True)
# find all the groups that add up to group weight
class GroupState:
  def __init__(self, packages):
    self.current_packages = copy.copy(packages)
    self.current_total = 0
    self.current_group = []

def product(list):
    p = 1
    for i in list:
        p *= i
    return p

# Add the biggest number available first and then cycle to the lower numbers
# At depth 6, we must add up to make 508
# If we can't, we are either 2 away or we are done
smallest_entanglement = 1000000000000000000
def add_package(group_state):
  global smallest_entanglement, groups
  if len(group_state.current_group) == 4:
    #one more to add
    num_left = group_weight - group_state.current_total
    if num_left == 2:
      return True
    if num_left not in group_state.current_packages:
      return True
    group = copy.copy(group_state.current_group)
    group.append(num_left)
    # print group
    entanglement = product(group)
    if entanglement < smallest_entanglement:
      smallest_entanglement = entanglement
      print group
      print smallest_entanglement
    return True
  else:
    for package in group_state.current_packages:
      state = copy.deepcopy(group_state)
      state.current_total += package
      state.current_group.append(package)
      state.current_packages.remove(package)
      if state.current_total > group_weight or len(state.current_group) > 5:
        return True
      status = add_package(state)
      if not status:
        return False
  return True

state = GroupState(packages)
add_package(state)
print biggest_entanglement