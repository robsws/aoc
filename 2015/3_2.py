#!/usr/local/bin/python
import sys
import math

houses_delivered_to = {"0,0": 1} # one present delivered to index (0,0)
current_locations = [[0,0],[0,0]]
file = open("3_input.txt",'r')
current_santa = 0

def deliver_present(santa_number):
  # add the house to the list of houses visited
  house_key = str(current_locations[santa_number][0])+","+str(current_locations[santa_number][1])
  houses_delivered_to[house_key] = 1

def up(santa_number):
  # santa moves up
  current_locations[santa_number][1] += 1

def down(santa_number):
  # santa moves down
  current_locations[santa_number][1] -= 1

def left(santa_number):
  # santa moves left
  current_locations[santa_number][0] -= 1

def right(santa_number):
  # santa moves right
  current_locations[santa_number][0] += 1

commands = {
  '^': up,
  'v': down,
  '<': left,
  '>': right,
}

for line in file:
  for command in line:
    commands[command](current_santa)
    deliver_present(current_santa)
    if current_santa == 0:
      current_santa = 1
    else:
      current_santa = 0

print "Amount of houses visited: "+str(len(houses_delivered_to.keys()))