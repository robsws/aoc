#!/usr/local/bin/python
import sys
import pprint
from random import shuffle
pp = pprint.PrettyPrinter(indent=4)
file = open(sys.argv[1], 'r')
# BST one location at at a time
# Generate a new bot for each possible path
# If you return to a previous point, delete the bot
# If a bot finds a node already visited by another bot, delete the bot
# If two bots end up on the same location, delete one of the bots

# Start at the 0 and visit all non-0 numbers
locations = {}
maze = []
for y, line in enumerate(file):
  row = []
  line = line.rstrip()
  for x, char in enumerate(line):
    if char == '#':
      row.append(-1)
    elif char == '.':
      row.append(0)
    elif char == '0':
      loc = 8
      locations[loc] = [x,y]
      row.append(8)
    else:
      loc = int(char)
      locations[loc] = [x,y]
      row.append(int(char))
  maze.append(row)
maze = list(zip(*maze))

graph = {}
for i in range(1,9):
  graph[i] = {}
  for j in range(1,9):
    graph[i][j] = -1

def next_bots(start_loc, bots, visited):
  global graph
  locations_found = []
  new_bots = []
  for bot in bots:
    pos = bot['coord']
    if pos[1] > 0 and maze[pos[0]][pos[1]-1] >= 0 and str(pos[0])+','+str(pos[1]-1) not in visited:
      # up
      new_bot = {
        'coord': [pos[0],pos[1]-1],
        'distance': bot['distance'] + 1
      }
      location = maze[new_bot['coord'][0]][new_bot['coord'][1]]
      if location > 0:
        graph[start_loc][location] = new_bot['distance']
        locations_found.append(location)
        print("found "+str(location))
      new_bots.append(new_bot)
      visited.add(str(pos[0])+','+str(pos[1]-1))
    if pos[1] < len(maze)-1 and maze[pos[0]][pos[1]+1] >= 0 and str(pos[0])+','+str(pos[1]+1) not in visited:
      # down
      new_bot = {
        'coord': [pos[0],pos[1]+1],
        'distance': bot['distance'] + 1
      }
      location = maze[new_bot['coord'][0]][new_bot['coord'][1]]
      if location > 0:
        graph[start_loc][location] = new_bot['distance']
        locations_found.append(location)
        print("found "+str(location))
      new_bots.append(new_bot)
      visited.add(str(pos[0])+','+str(pos[1]+1))
    if pos[0] > 0 and maze[pos[0]-1][pos[1]] >= 0 and str(pos[0]-1)+','+str(pos[1]) not in visited:
      # left
      new_bot = {
        'coord': [pos[0]-1,pos[1]],
        'distance': bot['distance'] + 1
      }
      location = maze[new_bot['coord'][0]][new_bot['coord'][1]]
      if location > 0:
        graph[start_loc][location] = new_bot['distance']
        locations_found.append(location)
        print("found "+str(location))
      new_bots.append(new_bot)
      visited.add(str(pos[0]-1)+','+str(pos[1]))
    if pos[1] < len(maze[0])-1 and maze[pos[0]+1][pos[1]] >= 0 and str(pos[0]+1)+','+str(pos[1]) not in visited:
      # right
      new_bot = {
        'coord': [pos[0]+1,pos[1]],
        'distance': bot['distance'] + 1
      }
      location = maze[new_bot['coord'][0]][new_bot['coord'][1]]
      if location > 0:
        graph[start_loc][location] = new_bot['distance']
        locations_found.append(location)
        print("found "+str(location))
      new_bots.append(new_bot)
      visited.add(str(pos[0]+1)+','+str(pos[1]))
  return (visited, locations_found, new_bots)

finished = False
total_distance = 0

for i in range(1,9):
  print("start: "+str(i))
  bots = [{'coord':locations[i], 'distance':0}]
  visited = set([str(locations[i][0]) + ',' + str(locations[i][1])])
  locations_found = []
  while len(locations_found) < 7:
    (visited, new_locations_found, bots) = next_bots(i, bots, visited)
    if new_locations_found:
      locations_found.extend(new_locations_found)

pp.pprint(graph)

# Randomly pick paths until we get the best
shortest_distance = 10000000
while True:
  locations_list = [1,2,3,4,5,6,7]
  shuffle(locations_list)
  locations_list.append(8)
  locations_list.insert(0,8)
  total_distance = 0
  for i in range(0, 8):
    total_distance += graph[locations_list[i]][locations_list[i+1]]
  if total_distance < shortest_distance:
    shortest_distance = total_distance
    print(shortest_distance)

# graph_flat = {}
# for i in range(1,9):
#   for j in range(1,9):
#     if j > i:
#       graph_flat[str(i)+','+str(j)] = graph[i][j]

# for i in sorted(graph_flat.items(), key=lambda x: x[1]):
#   print(i)