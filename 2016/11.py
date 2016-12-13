#!/usr/local/bin/python
from copy import deepcopy
import pprint
import sys

start_state_part1 = {
  1: ['SG','SM','PG','PM'],
  2: ['TG','RG','RM','CG','CM'],
  3: ['TM'],
  4: [],
  'Elevator': 1
}

start_state_part2 = {
  1: ['SG','SM','PG','PM','EG','EM','DG','DM'],
  2: ['TG','RG','RM','CG','CM'],
  3: ['TM'],
  4: [],
  'Elevator': 1
}

final_state_key = 'E41234CGCMPGPMRGRMSGSMTGTM'

def valid_floor(items):
  # Check for M without matching G where a G of different type exists
  for item in items:
    if item[1] == 'M':
      if item[0]+'G' not in items:
        for second_item in items:
          if second_item[1] == 'G':
            return False
  return True

def serialise_state(state):
  # Serialise the state
  state_key = 'E'+str(state['Elevator'])
  for floor in range(1, 5):
    state_key += str(floor)
    state_key += reduce(lambda x,y: x+y, sorted([''] + state[floor]))
  return state_key

state_cache = {}

def seen_state_already(state_key):
  # Check the map for membership
  if state_key in state_cache:
    return True
  else:
    state_cache[state_key] = 1
    return False

def reached_final_state(state_key):
  # Check if this is the final state
  return state_key == final_state_key

def possible_next_states(current_state):
  reached_final = False
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
  
  # Eliminate more possibilities by taking cargo into account
  next_states = []
  for floor in next_elevator_values:
    for cargo in possible_cargo_permutations:
      # Figure out what the new floor will look like with cargo added
      new_floor_items = list(current_state[floor])
      new_floor_items.extend(cargo)
      # Make sure the new floor is a valid combination of cargo
      if valid_floor(new_floor_items):
        # Create a new state
        next_state = deepcopy(current_state)
        next_state['Elevator'] = floor
        # Copy cargo to new floor
        next_state[floor] = new_floor_items
        # Remove cargo from current floor
        map(lambda x: next_state[current_floor].remove(x), cargo)
        # Make sure the floor we removed cargo from is still valid and
        # don't go back to previously visited states
        state_key = serialise_state(next_state)
        if valid_floor(next_state[current_floor]) and not seen_state_already(state_key):
          # Check if we have reached the end
          reached_final = reached_final_state(state_key)
          if reached_final:
            print("reached_final")
          # Add the new state to the list of possible next states
          next_states.append(next_state)
  return [reached_final, next_states]

# Perform a breadth-first search through the possible moves
states = []
if sys.argv[1] == '2':
  states.append(start_state_part2)
else:
  states.append(start_state_part1)
reached_final = False
iterations = 0
while not reached_final:
  (reached_final, states) = reduce(lambda x,y: [x[0] or y[0], x[1] + y[1]], map(lambda state: possible_next_states(state), states))
  iterations += 1
  print(str(iterations)+" complete.")
print("shortest path: "+str(iterations))