#!/usr/local/bin/python
import sys
import math

houses_delivered_to = {"0,0": 1} # one present delivered to index (0,0)
current_location = [0,0]
file = open("3_input.txt",'r')

def deliver_present():
  # add the house to the list of houses visited
  house_key = str(current_location[0])+","+str(current_location[1])
  houses_delivered_to[house_key] = 1

def up():
  # santa moves up
  current_location[1] += 1

def down():
  # santa moves down
  current_location[1] -= 1

def left():
  # santa moves left
  current_location[0] -= 1

def right():
  # santa moves right
  current_location[0] += 1

commands = {
  '^': up,
  'v': down,
  '<': left,
  '>': right,
}

for line in file:
  for command in line:
    commands[command]()
    deliver_present()

print "Amount of houses visited: "+str(len(houses_delivered_to.keys()))