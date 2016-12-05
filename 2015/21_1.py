#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

player = {
  "hp": 100,
  "atk": 0,
  "def": 0
}

boss = {
  "hp": 100,
  "atk": 8,
  "def": 2
}

shop = {}
file = open('21_input.txt', 'r')
for line in file:
  (name, cost, atk, defense) = line.split(',')
  item = {
    "cost": int(cost),
    "atk": int(atk),
    "def": int(defense),
  }
  if name not in shop.keys():
    shop[name] = []
  shop[name].append(item)
for item_type in shop.keys():
  shop[item_type].sort(key=operator.itemgetter('cost'))

# for item_type in shop.keys():
#   for item in shop[item_type]:
#     print item

# Figure out the most cost effective way of making up the discrepancy
# Loop through the possible item combinations, starting with the cheapest
index_types = ["Weapon", "Armour", "Ring", "Ring"]
current_combination = [0,-1,-1,-1]
combinations = []

def fight(stats):
  return (stats["atk"]-boss["def"]) - (boss["atk"]-stats["def"])

def next_combination(combination, index_types):
  combination[0] += 1
  # print len(shop(index_types[0]))
  if combination[0] >= len(shop[index_types[0]]):
    combination[0] = -1
    if len(combination) == 1:
      return combination
    next_index_types = copy.deepcopy(index_types[1:])
    next_combo = copy.deepcopy(combination[1:])
    subcombo = next_combination(next_combo, next_index_types)
    subcombo.insert(0, combination[0])
    return subcombo
  return combination

best_cost = 10000000
best_combo = []
best_stats = {}
while current_combination != [-1,-1,-1,-1]:
  # calculate new player atk/def and cost
  stats = {
    "atk": player["atk"],
    "def": player["def"],
    "cost": 0
  }
  # print current_combination
  for index, item in enumerate(current_combination):
    if item != -1:
      # print shop[index_types[index]][item]["cost"]
      stats["cost"] += shop[index_types[index]][item]["cost"]
      stats["atk"] += shop[index_types[index]][item]["atk"]
      stats["def"] += shop[index_types[index]][item]["def"]
  # if the new stats would beat the boss, add it to the list
  # print "total: "+str(stats["cost"])
  if stats["cost"] < best_cost and fight(stats) >= 0:
    best_cost = stats["cost"]
    best_combo = copy.deepcopy(current_combination)
    best_stats = copy.deepcopy(stats)
  # iterate combination
  current_combination = next_combination(copy.deepcopy(current_combination), copy.deepcopy(index_types))

print best_cost
print best_combo
print best_stats