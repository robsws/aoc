import sys
import re
import time

input_filename = sys.argv[1]
file = open(input_filename,'r')

input_regex = re.compile(r'^p=<(-?\d+),(-?\d+),(-?\d+)>. v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>$')

particles = []

for i, line in enumerate(file.read().splitlines()):
    match = re.search(input_regex, line)
    if match:
        (pos_x, pos_y, pos_z, vel_x, vel_y, vel_z, acc_x, acc_y, acc_z) = list(map(int, match.groups()))
        particles.append({
            'position'     : [pos_x, pos_y, pos_z],
            'velocity'     : [vel_x, vel_y, vel_z],
            'acceleration' : [acc_x, acc_y, acc_z]
        })

for i in range(1000):
    for particle in particles:
        particle['velocity'][0] += particle['acceleration'][0]
        particle['velocity'][1] += particle['acceleration'][1]
        particle['velocity'][2] += particle['acceleration'][2]
        particle['position'][0] += particle['velocity'][0]
        particle['position'][1] += particle['velocity'][1]
        particle['position'][2] += particle['velocity'][2]
    sorted_particles = sorted(particles, key=lambda k: k['position'])

min_distance = 9999999999
min_distance_particle = 0
for i, particle in enumerate(particles):
    distance_from_origin = sum(list(map(abs, particle['position'])))
    if distance_from_origin < min_distance:
        min_distance = distance_from_origin
        min_distance_particle = i

print('part 1:',min_distance_particle)