#!/usr/local/bin/python
from functools import reduce
input_data = '01111010110010011'
disk_size = 35651584

def expand(data):
  ret = data + '0'
  data_b = data[::-1]
  for bit in data_b:
    ret += '0' if bit == '1' else '1'
  #data_b = reduce(lambda x,y: x+y, ['0' if bit == '1' else '1' for bit in data_b])
  return ret

def calculate_checksum(data):
  checksum = ''
  if len(data) % 2 != 0:
    return data
  else:
    for i in xrange(0, len(data), 2):
      if data[i] == data[i+1]:
        checksum += '1'
      else:
        checksum += '0'
    return calculate_checksum(checksum)

while(len(input_data) < disk_size):
  input_data = expand(input_data)

print(calculate_checksum(input_data[0:disk_size]))
