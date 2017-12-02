#!/usr/local/bin/python
import sys
import re

part = int(sys.argv[1])
input_filename = sys.argv[2]
file = open(input_filename,'r')

def calculate_row_checksum(row, part):
    if part == 1:
        return max(row) - min(row)
    else:
        row.sort(reverse=True)
        for i in range(len(row)):
            for j in range(i+1, len(row)):
                if(row[i] % row[j] == 0):
                    return int(row[i] / row[j])

split_regex = re.compile(r"\s+")
checksum = 0
for line in file:
    line = line.rstrip("\n")
    row = list(map(int, split_regex.split(line)))
    checksum += calculate_row_checksum(row, part)
print(checksum)