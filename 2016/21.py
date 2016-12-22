#!/usr/local/bin/python
import sys
import re
file = open(sys.argv[1], 'r')
password = 'cegdahbf'

swap_pos_re = re.compile(r'^swap position (\d+) with position (\d+)')
swap_char_re = re.compile(r'^swap letter (\w) with letter (\w)')
rotate_dir_re = re.compile(r'^rotate (left|right) (\d+) steps?')
rotate_pos_re = re.compile(r'^rotate based on position of letter (\w)')
reverse_re = re.compile(r'^reverse positions (\d+) through (\d+)')
move_re = re.compile(r'^move position (\d+) to position (\d+)')

def swap_position(password, index1, index2):
  password = list(password)
  swap = password[index1]
  password[index1] = password[index2]
  password[index2] = swap
  return "".join(password)

def swap_letter(password, letter1, letter2):
  index1 = password.index(letter1)
  index2 = password.index(letter2)
  return swap_position(password, index1, index2)

def rotate(password, direction, amount):
  password = list(password)
  if direction == 'left':
    password.reverse()
  for i in range(amount):
    letter = password.pop()
    password.insert(0, letter)
  if direction == 'left':
    password.reverse()
  return "".join(password)

def rotate_by(password, letter):
  amount = 1
  index = password.index(letter)
  if index >= 4:
    amount += 1
  amount += index
  return rotate(password, 'right', amount)

def reverse(password, index1, index2):
  password = list(password)
  substr = password[index1:index2+1]
  substr.reverse()
  return "".join(password[:index1] + substr + password[index2+1:])

def move(password, index1, index2):
  password = list(password)
  letter = password[index1]
  password = password[:index1] + password[index1+1:]
  password.insert(index2, letter)
  return "".join(password)

for line in file:
  print(password)
  print(line.rstrip())
  match = re.match(swap_pos_re, line)
  if match:
    (index1, index2) = match.groups()
    password = swap_position(password, int(index1), int(index2))
    continue
  match = re.match(swap_char_re, line)
  if match:
    (letter1, letter2) = match.groups()
    password = swap_letter(password, letter1, letter2)
    continue
  match = re.match(rotate_dir_re, line)
  if match:
    (direction, amount) = match.groups()
    password = rotate(password, direction, int(amount))
    continue
  match = re.match(rotate_pos_re, line)
  if match:
    letter = match.group(1)
    password = rotate_by(password, letter)
    continue
  match = re.match(reverse_re, line)
  if match:
    (index1, index2) = match.groups()
    password = reverse(password, int(index1), int(index2))
    continue
  match = re.match(move_re, line)
  if match:
    (index1, index2) = match.groups()
    password = move(password, int(index1), int(index2))
    continue
print(password)