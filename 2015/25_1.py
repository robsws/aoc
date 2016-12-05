#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy
from operator import mul

# First figure out the number of the code
# First row is triangle numbers, then columns add number of the column first
# and then add an incremented number
# row = 2981
# column = 3075
row = int(sys.argv[1])
column = int(sys.argv[2])

column_first_num = int((row*(row+1))/2.0)
num = column_first_num
inc = row
for i in range(column-1):
  num += inc
  inc += 1

code = 20151125
for i in range(num-1):
  code *= 252533
  code = code % 33554393
print code