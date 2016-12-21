#!/usr/local/bin/python
import sys
from math import floor
no_of_elves = int(sys.argv[1])
# removed_elves = set()
# all_elves = range(0, no_of_elves)
# i = 0
# j = 0
# while len(removed_elves) < no_of_elves - 1:
#   print("****")
#   print("Current elf: "+str(i)+" Index: "+str(j))
#   remaining_elves = no_of_elves - len(removed_elves)
#   if i not in removed_elves:
#     # Loop forward floor(n/2) times
#     found = 0
#     for j in range(no_of_elves):
#       index = (i + j) % no_of_elves
#       if j not in removed_elves:
#         found += 1
#         if found == floor(removed_elves/2)
#     removed_elves.add(elf_to_remove)
#   i = (i + 1) % no_of_elves
#   print(removed_elves)

# remaining = [item for item in all_elves if item not in removed_elves]
# print(remaining[0])

# elves = range(0, no_of_elves)
# i = 0 # position in overall list
# j = 0 # position in actual list
# iter = 0
# removed = set()
# while len(removed) < no_of_elves - 1:
#   # print
#   # print("i: "+str(i))
#   # print("j: "+str(j))
#   # print(removed)
#   if i not in removed:
#     if(iter % 10 == 0):
#       print("iter: "+str(iter))
#     elf_to_remove = i
#     for k in range(int(floor(no_of_elves - len(removed))/2)):
#       elf_to_remove = (elf_to_remove + 1) % no_of_elves
#       while elf_to_remove in removed:
#         elf_to_remove = (elf_to_remove + 1) % no_of_elves
#     # actual_elves = [elf for elf in elves if elf not in removed]
#     # elf_to_remove = (j + (int(floor(len(actual_elves)/2)))) % len(actual_elves)
#     # print('elf to remove: '+ str(elf_to_remove))
#     # print('removing '+str(actual_elves[elf_to_remove]))
#     removed.add(elves[elf_to_remove])
#     # del elves[elf_to_remove]
#     if elf_to_remove > j:
#       j = (j+1) % len(elves)
#     else:
#       j = j % len(elves)
#   i = (i+1) % no_of_elves
#   iter += 1
# remaining = [elf for elf in elves if elf not in removed]
# print(remaining[0]+1)

def solve_circle(elves):
  offset = 2
  no_of_elves = len(elves)
  if no_of_elves % 2 == 1:
    offset = 1
  digital_half = int(floor(no_of_elves/2))
  index = digital_half
  next_elves = []
  for i in range(no_of_elves):
    elf = (i+index) % no_of_elves
    if (i-offset) % 3 == 0 or (elf + 1 == digital_half and (no_of_elves % 3 == 1 or no_of_elves % 3 == 2)):
      next_elves.append(elves[elf])
  new_dig_half = int(floor(len(next_elves)/2))
  next_elves = next_elves[new_dig_half:] + next_elves[:new_dig_half]
  return next_elves
elves = range(0, no_of_elves)
while len(elves) > 1:
  # print(elves)
  elves = solve_circle(elves)
print(elves)
