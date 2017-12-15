import sys
from knot_hash import knot_hash

input_filename = sys.argv[1]
file = open(input_filename,'r')
plaintext = file.read().rstrip()

print('part2: '+knot_hash(plaintext))