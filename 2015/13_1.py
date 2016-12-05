#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

file = open("13_input.txt",'r')

regex = re.compile(r'^([A-Za-z]+) would (gain|lose) ([0-9]+) happiness units by sitting next to ([A-Za-z]+).$')

# Parsing
guests = {}
for line in file:
  match = re.search(regex, line)
  (guest, plusminus, happiness, neighbour) = match.groups()
  if guest not in guests.keys():
    guests[guest] = {}
  happiness = int(happiness)
  if plusminus == "lose":
    happiness = -happiness
  guests[guest][neighbour] = happiness

# Add myself to the list
guests['Rob'] = {}
for guest in guests.keys():
  guests['Rob'][guest] = 0
  guests[guest]['Rob'] = 0

# Calculate scores of pairs
pairs = {}
for guest1 in guests.keys():
  pairs[guest1] = {}
  for guest2 in guests.keys():
    if guest1 == guest2:
      continue
    pairs[guest1][guest2] = guests[guest1][guest2] + guests[guest2][guest1]
    print guest1 + "-" + guest2 + ": " + str(pairs[guest1][guest2])

# Calculate seating arrangement
best_arrangement = []
best_score = 0
def choose_next_neighbour(guest, seated_guests, current_score):
  global best_arrangement, best_score
  choices = pairs[guest]
  for next_guest in choices.keys():
    if next_guest in seated_guests:
      if len(seated_guests) == len(guests.keys()) and next_guest == seated_guests[0]:
        new_seating = copy.deepcopy(seated_guests)
        new_seating.append(next_guest)
        new_score = current_score + choices[next_guest]
        if new_score > best_score:
          best_arrangement = new_seating
          best_score = new_score
          print "New Best Arrangement"
          print best_arrangement
          print best_score
      else:
        continue
    else:
      new_seating = copy.deepcopy(seated_guests)
      new_seating.append(next_guest)
      new_score = current_score + choices[next_guest]
      if len(new_seating) <= len(guests.keys()):
        choose_next_neighbour(next_guest, new_seating, new_score)

for guest in guests.keys():
  choose_next_neighbour(guest, [guest], 0)