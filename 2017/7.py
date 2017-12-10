#!/usr/local/bin/python
import sys
import re
from collections import Counter

input_filename = sys.argv[1]
file = open(input_filename,'r')
weight_regex = re.compile(r"^(\w+) \((\d+)\)")
child_regex = re.compile(r"(\w+)")

weights = dict()
subtowers = dict()

for line in file:
    parts = line.split('->')
    weight_match = re.search(weight_regex, parts[0])
    (program, weight) = weight_match.groups()
    if len(parts) > 1:
        children = child_regex.findall(parts[1])
        subtowers[program] = children
    weights[program] = int(weight)

total_weights = dict()
def generate_total_weights(program):
    if program not in subtowers.keys():
        total_weights[program] = weights[program]
    else:
        for subtower in subtowers[program]:
            generate_total_weights(subtower)
        total_weights[program] = weights[program] + sum([total_weights[x] for x in subtowers[program]])

root = 'cqmvs' # root of the tree
# root = 'tknk'
generate_total_weights(root)

def find_unbalanced(program):
    if program not in subtowers.keys():
        return False
    for subtower in subtowers[program]:
        other_towers = [y for y in subtowers[program] if y != subtower]
        if all(total_weights[subtower] != total_weights[x] for x in other_towers):
            if find_unbalanced(subtower):
                for subtower in subtowers[program]:
                    print(subtower + ' ' + str(total_weights[subtower]))
                return False
    return True

find_unbalanced(root)