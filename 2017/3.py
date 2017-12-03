#!/usr/local/bin/python
import sys

part = int(sys.argv[1])
input_val = int(sys.argv[2])

if input_val == 1:
    return 0

# Find the largest square number whose root is odd
# smaller than input
largest_square = 0
layer = 0
i = 1
while True:
    next_square = i ** 2
    if next_square >= input_val:
        break
    largest_square = next_square
    layer += 1
    i += 2

# Track the number around the outside of the square
j = largest_square + 1
distance = 2*layer - 1
direction = -1
while j < input_val:
    if distance == layer or distance == layer*2:
        direction *= -1
    distance += direction
    j += 1

print(distance)