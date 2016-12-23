#!/usr/local/bin/python
import sys
import hashlib
import re
from copy import deepcopy

passcode = sys.argv[1]
door_open_regex = re.compile(r'[bcdef]')

def create_new_path(path, coord):
  new_path = {
    'path': path,
    'coord': coord
  }
  if new_path['coord'] == [3,3]:
    print(len(new_path['path']))
    return None
  else:
    return new_path

def expand_paths(paths):
  new_paths = []
  for path in paths:
    plaintext = passcode + path['path']
    hashtext = hashlib.md5(plaintext.encode('utf-8')).hexdigest()
    if path['coord'][1] > 0 and re.match(door_open_regex, hashtext[0]):
      # up
      new_path = create_new_path(path['path'] + 'U', [path['coord'][0], path['coord'][1]-1])
      if new_path:
        new_paths.append(new_path)
    if path['coord'][1] < 3 and re.match(door_open_regex, hashtext[1]):
      # down
      new_path = create_new_path(path['path'] + 'D', [path['coord'][0], path['coord'][1]+1])
      if new_path:
        new_paths.append(new_path)
    if path['coord'][0] > 0 and re.match(door_open_regex, hashtext[2]):
      # left
      new_path = create_new_path(path['path'] + 'L', [path['coord'][0]-1, path['coord'][1]])
      if new_path:
        new_paths.append(new_path)
    if path['coord'][0] < 3 and re.match(door_open_regex, hashtext[3]):
      #right
      new_path = create_new_path(path['path'] + 'R', [path['coord'][0]+1, path['coord'][1]])
      if new_path:
        new_paths.append(new_path)
  return new_paths

paths = [{'path': '', 'coord': [0,0]}]
finished = False
i = 1

while True:
  # print(i)
  # print("possible paths: "+str(len(paths)))
  paths = expand_paths(paths)
  i += 1