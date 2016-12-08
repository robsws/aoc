#!/usr/local/bin/python
import sys
import re

(prog, filename, width, height) = sys.argv
file = open(filename,'r')
rect_regex = re.compile(r"^rect (\d+)x(\d+)$")
rotate_regex = re.compile(r"^rotate (row|column) [xy]=(\d+) by (\d+)$")

def rotate_list_by_one(l):
  value = l.pop()
  l.insert(0,value)
  return l

class Screen:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.pixels = [[0 for y in range(height)] for x in range(width)]

  def rect(self, width, height):
    for x in range(width):
      for y in range(height):
        self.pixels[x][y] = 1

  def rotate_column(self, x, amount):
    for i in range(amount % self.height):
      self.pixels[x] = rotate_list_by_one(self.pixels[x])

  def rotate_row(self, y, amount):
    new_row = map(lambda x: x[y], self.pixels)
    for i in range(amount % self.width):
      new_row = rotate_list_by_one(new_row)
    for x,value in enumerate(new_row):
      self.pixels[x][y] = value

  def pixels_on(self):
    total = 0
    for column in self.pixels:
      for pixel in column:
        total += pixel
    return total

  def print_pixels(self):
    for y in range(self.height):
      row = map(lambda x: '.' if x[y] == 0 else 'X', self.pixels)
      print(reduce(lambda a,b: a+b, row))

screen = Screen(int(width), int(height))

for line in file:
  line = line.rstrip()
  match = re.search(rect_regex, line)
  if match:
    (rect_width, rect_height) = match.groups()
    screen.rect(int(rect_width), int(rect_height))
  else:
    match = re.search(rotate_regex, line)
    if match:
      (row_or_column, index, amount) = match.groups()
      if row_or_column == 'row':
        screen.rotate_row(int(index), int(amount))
      elif row_or_column == 'column':
        screen.rotate_column(int(index), int(amount))
  print(line)
  screen.print_pixels()

print(screen.pixels_on())