import sys
import re
import time
from itertools import tee

input_filename = sys.argv[1]
file = open(input_filename,'r')

input_regex = re.compile(r'^p=<(-?\d+),(-?\d+),(-?\d+)>. v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>$')

particles = {}

for i, line in enumerate(file.read().splitlines()):
    match = re.search(input_regex, line)
    if match:
        (pos_x, pos_y, pos_z, vel_x, vel_y, vel_z, acc_x, acc_y, acc_z) = list(map(int, match.groups()))
        particles[i] = {
            'position'     : [pos_x, pos_y, pos_z],
            'velocity'     : [vel_x, vel_y, vel_z],
            'acceleration' : [acc_x, acc_y, acc_z]
        }

for i in range(1000):
    if i % 1000 == 0:
        print(i)
    for key in particles:
        particles[key]['velocity'][0] += particles[key]['acceleration'][0]
        particles[key]['velocity'][1] += particles[key]['acceleration'][1]
        particles[key]['velocity'][2] += particles[key]['acceleration'][2]
        particles[key]['position'][0] += particles[key]['velocity'][0]
        particles[key]['position'][1] += particles[key]['velocity'][1]
        particles[key]['position'][2] += particles[key]['velocity'][2]

    sorted_particles = sorted(particles.keys(), key=lambda k: particles[k]['position'])
    iter1, iter2 = tee(sorted_particles, 2)
    next(iter2)
    indexes_to_delete = set()
    for pair in zip(iter1, iter2):
        if particles[pair[0]]['position'] == particles[pair[1]]['position']:
            indexes_to_delete.add(pair[0])
            indexes_to_delete.add(pair[1])
    for j in indexes_to_delete:
        del particles[j]

print('part 2:',len(particles))