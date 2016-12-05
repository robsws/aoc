#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

file = open("14_test_input.txt",'r')
total_time = int(sys.argv[1])

regex = re.compile(r'([A-Za-z]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds')

# Parsing
reindeer = {}
for line in file:
  match = re.search(regex, line)
  (name, speed, flying_time, resting_time) = match.groups()
  reindeer[name] = {
    "speed": int(speed),
    "flying_time": int(flying_time),
    "resting_time": int(resting_time),
    "points": 0
  }

def distance_travelled(name, time):
  current_reindeer = reindeer[name]
  distance = 0
  cycle_length = current_reindeer["flying_time"] + current_reindeer["resting_time"]
  # calculate distance travelled in full cycles
  amount_of_full_cycles = int(math.floor(time / cycle_length))
  distance += amount_of_full_cycles * current_reindeer["speed"] * current_reindeer["flying_time"]
  # calculate distance travelled in partial cycle at the end
  remainder_time = time % cycle_length
  if remainder_time > current_reindeer["flying_time"]:
    remainder_time = current_reindeer["flying_time"]
  distance += current_reindeer["speed"] * remainder_time
  return distance

for t in range(1,total_time+1):
  best_distance = 0
  best_reindeer = ''
  for name in reindeer.keys():
    distance = distance_travelled(name, t)
    if distance > best_distance:
      best_distance = distance
      best_reindeer = name
  # print str(best_reindeer)+" "+str(best_distance)
  reindeer[best_reindeer]["points"] += 1

for name in reindeer.keys():
  print name+": "+str(reindeer[name]["points"])