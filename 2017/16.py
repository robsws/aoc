import sys
import re
from functools import reduce

input_filename = sys.argv[1]
file = open(input_filename,'r')
moves_input = file.read().rstrip()
moves_input = moves_input.split(',')
moves = []
dancers = list(map(chr, range(97, 113)))

def spin(x):
    dancers[0:0] = dancers[-x:]
    del dancers[-x:]

def exchange(a, b):
    tmp = dancers[a]
    dancers[a] = dancers[b]
    dancers[b] = tmp

def partner(a, b):
    exchange(dancers.index(a), dancers.index(b))

# parse instructions
print('parse instructions')
spin_regex     = re.compile(r'^s(\d+)$')
exchange_regex = re.compile(r'^x(\d+)/(\d+)$')
partner_regex  = re.compile(r'^p(\w)/(\w)$')
for move in moves_input:
    match = re.search(spin_regex, move)
    if match:
        (x,) = match.groups()
        moves.append((spin, (int(x),)))
        continue
    match = re.search(exchange_regex, move)
    if match:
        (a, b) = match.groups()
        moves.append((exchange, (int(a), int(b))))
        continue
    match = re.search(partner_regex, move)
    if match:
        (a, b) = match.groups()
        moves.append((partner, (a, b)))
        continue

def dancers_to_string(dancers):
    return reduce(lambda x, y: x + y, dancers)

# run instructions
print('run instructions')
dance_patterns = [dancers_to_string(dancers)]
for i in range(1000000000):
    for func, args in moves:
        func(*args)
    if dancers_to_string(dancers) == 'abcdefghijklmnop':
        break
    dance_patterns.append(dancers_to_string(dancers))        

answer_index = 1000000000 % len(dance_patterns)

print('part 1: '+dancers_to_string(dance_patterns[1]))
print('part 2: '+dancers_to_string(dance_patterns[answer_index]))