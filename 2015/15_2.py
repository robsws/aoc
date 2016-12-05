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
    "teaspoons": 0,
    "calories": int(calories)
  }

# Work out which combinations of ingredients make 500 calories
all_combos = []
def find_combos(full_ingredients, current_ingredients, current_calorie_total, current_teaspoon_total):
  global all_combos
  # print len(current_ingredients)
  ingredient = current_ingredients.keys()[0]
  combos = []
  if len(current_ingredients) == 1:
    # base case, we need to sum up the teaspoons to 100
    teaspoons_left = 100 - current_teaspoon_total
    full_ingredients[ingredient]["teaspoons"] = teaspoons_left
    calories = current_calorie_total + current_ingredients[ingredient]["calories"] * teaspoons_left
    if calories == 500:
      all_combos.append(copy.deepcopy(full_ingredients))
    return
  for amount in range(100 + 1):
    # still more than 1 ingredient left to allocate
    calories = current_calorie_total + current_ingredients[ingredient]["calories"] * amount
    teaspoons = current_teaspoon_total + amount
    if calories > 500 or teaspoons >= 100:
      continue
    full_ingredients[ingredient]["teaspoons"] = amount
    next_ingredients = copy.deepcopy(current_ingredients)
    next_ingredients.pop(ingredient, None)
    find_combos(full_ingredients, next_ingredients, calories, teaspoons)

find_combos(copy.deepcopy(ingredients), copy.deepcopy(ingredients), 0, 0)

# Find the optimal combo
best_score = 0
for combo in all_combos:
  property_totals = {
    "capacity": 0,
    "durability": 0,
    "flavor": 0,
    "texture": 0
  }
  for ing in combo:
    for prop in property_totals.keys():
      property_totals[prop] += combo[ing][prop] * combo[ing]["teaspoons"]
  total_score = 1
  for score in property_totals.values():
    total_score *= score
  if total_score > best_score:
    best_score = total_score

print best_score