#!/usr/local/bin/python
import sys
from collections import defaultdict

part = int(sys.argv[1])
input_filename = sys.argv[2]
file = open(input_filename,'r')

valid_total = 0
for line in file:
    line = line.rstrip("\n")
    words = line.split(' ')
    unique_words = set()
    if part == 1:
        unique_words = {x for x in words}
    else:
        unique_words = {str(sorted(x)) for x in words}
    if len(unique_words) == len(words):
        valid_total += 1
print(valid_total)