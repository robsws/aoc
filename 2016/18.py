#!/usr/local/bin/python
previous_row = "^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^";
safe_tiles = previous_row.count('.')
previous_row = map(lambda x: True if x == '^' else False, previous_row)
for i in range(399999):
  row = []
  if i % 10000 == 0:
    print(i)
  # print(previous_row)
  for j in range(len(previous_row)):
    left = False
    right = False
    if j != 0:
      left = previous_row[j-1]
    if j != len(previous_row)-1:
      right = previous_row[j+1]
    if (left and not right) or (not left and right):
      row.append(True)
    else:
      row.append(False)
      safe_tiles += 1
  previous_row = row
print(safe_tiles)