#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

file = open("9_input.txt",'r')

regex = re.compile(r'^([A-Za-z]+) to ([A-Za-z]+) = ([0-9]+)$')
edges = []
cities = {}

all_locations = []
for line in file:
  # parse the line
  match = re.search(regex, line)
  (location_a, location_b, distance) = match.groups()
  distance = int(distance)
  if location_a not in all_locations:
    all_locations.append(location_a)
    cities[location_a] = {}
  if location_b not in all_locations:
    all_locations.append(location_b)
    cities[location_b] = {}
  cities[location_a][location_b] = distance
  cities[location_b][location_a] = distance
  

best_total_distance = 100000
best_route = []

# find the shortest path with branch and bound
def find_next_city(city, current_route, current_cost):
  global best_total_distance, best_route
  choices = cities[city]
  for next_city in choices.keys():
    if current_cost + choices[next_city] > best_total_distance \
    or next_city in current_route:
      continue
    new_route = copy.deepcopy(current_route)
    new_route.append(next_city)
    new_cost = current_cost + choices[next_city]
    if len(new_route) == len(all_locations):
      print "New Best Route!"
      print new_route
      print "Cost: " + str(new_cost)
      best_total_distance = new_cost
      best_route = new_route
    else:
      find_next_city(next_city, new_route, new_cost)

for city in all_locations:
  find_next_city(city, [city], 0)