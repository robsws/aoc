#!/usr/local/bin/python
from copy import deepcopy

start_state = {
  1: ['SG','SM','PG','PM'],
  2: ['TG','RG','RM','CG','CM'],
  3: ['TM'],
  4: [],
  'Elevator': 1
}

def valid_floor(items):
  # Check for M without matching G where a G of different type exists
  for item in items:
    if item[1] == 'M':
      if item[0]+'G' not in items:
        for second_item in items:
          if second_item[1] == 'G':
            return False
  return True

def possible_next_states(current_state):
  # Elevator must move up one or down one
  next_elevator_values = []
  if current_state['Elevator'] != 1:
    # Can go down in the elevator
    next_elevator_values.append(current_state['Elevator'] - 1)
  if current_state['Elevator'] != 4:
    # Can go up in the elevator
    next_elevator_values.append(current_state['Elevator'] + 1)

  # Work out all the permutations of items that could move in the elevator
  possible_cargo_permutations = []
  current_floor = current_state['Elevator']
  for i,first_elem in enumerate(current_state[current_floor]):
    possible_cargo_permutations.append([first_elem])
    for j,second_elem in enumerate(current_state[current_floor]):
      # Check either the first or second char are the same, otherwise
      # it will always be an illegal move.
      if i < j and (first_elem[0] == second_elem[0] or first_elem[1] == second_elem[1]):
        possible_cargo_permutations.append([first_elem,second_elem])
  
  # Eliminate more possibilities by checking what is on the floor we are moving
  # to.
  next_states = []
  for floor in next_elevator_values:
    for cargo in possible_cargo_permutations:
      new_floor_items = list(current_state[floor]).extend(cargo) # start here
      print(floor)
      if valid_floor(new_floor_items):
        next_state = deepcopy(current_state)
        next_state['Elevator'] = floor
        next_state[floor] = new_floor_items
        next_states.append(next_state)
  return next_states

print(possible_next_states(start_state))