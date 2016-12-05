#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

file = open("15_input.txt",'r')

regex = re.compile(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')

# Parsing
ingredients = {}
for line in file:
  match = re.search(regex, line)
  (ingredient, capacity, durability, flavor, texture, calories) = match.groups()
  ingredients[ingredient] = {
    "capacity": int(capacity),
    "durability": int(durability),
    "flavor": int(flavor),
    "texture": int(texture),
    # Start with 1 of each ingredient
    "teaspoons": 1
  }

# Add the teaspoon that adds the most score to the total without hitting 0
# until we get to 100
property_totals = {
  "capacity": 0,
  "durability": 0,
  "flavor": 0,
  "texture": 0,
}
# Initialise properties with first teaspoon of each ingredient
for ingredient in ingredients.keys():
  for prop in ingredients[ingredient].keys():
    if prop == 'teaspoons':
      continue
    else:
      property_totals[prop] += ingredients[ingredient][prop]

# Add the rest of the teaspoons
for i in range(len(ingredients.keys()), 100):
  print i
  best_ingredient = ''
  best_score = 0
  for ingredient in ingredients.keys():
    new_properties = copy.deepcopy(property_totals)
    score = 1
    for prop in ingredients[ingredient].keys():
      if prop == 'teaspoons':
        continue
      new_properties[prop] += ingredients[ingredient][prop]
      score = score * new_properties[prop]
    if score > best_score:
      best_ingredient = ingredient
      best_score = score
  if best_score == 0:
    raise Exception("No good choice")
  ingredients[best_ingredient]["teaspoons"] += 1
  print "Best score: "+str(best_score)
  for prop in ingredients[ingredient].keys():
    if prop == 'teaspoons':
      continue
    else:
      property_totals[prop] += ingredients[best_ingredient][prop]

# Print result
for ingredient in ingredients.keys():
  print ingredient+": "+str(ingredients[ingredient]["teaspoons"])