import sys
from functools import reduce

def zerofill(s):
    while len(s) < 2:
        s = '0' + s
    return s

def knot_hash(plaintext):
    # first convert plaintext to list of lengths needed for hash algorithm
    lengths = list(map(ord, plaintext)) + [17, 31, 73, 47, 23]
    knot = list(range(256))
    index = 0
    skip = 0

    # calculate the sparse hash
    for i in range(64):
        for length in lengths:
            # reverse the order of the elements in sublist
            if index + length > len(knot):
                reversed_section = list(reversed(knot[index:index+length] + knot[0:(index+length)-len(knot)]))
                knot[index:index+length] = reversed_section[0:len(knot) - index]
                knot[0:(index + length) - len(knot)] = reversed_section[len(knot) - index:]
            else:
                knot[index:index+length] = list(reversed(knot[index:index+length]))
            # move current position by length + skip
            index += length + skip
            if index > len(knot):
                index = index % len(knot)
            # increment skip by one
            skip += 1
    
    # calculate the list of numbers for the dense hash
    chunk_size = 16
    dense_hash_list = list()
    for chunk in [knot[i:i+chunk_size] for i in range(0, len(knot), chunk_size)]:
        dense_hash_list.append(reduce(lambda x, y: x ^ y, chunk))
    
    # build hexadecimal dense hash
    return reduce(lambda x, y: x + y, map(lambda x: zerofill(hex(x)[2:]), dense_hash_list))