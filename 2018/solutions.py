from utils import *
from collections import defaultdict
from itertools import chain
import re

# Day One Solutions
def sum_frequencies(inputs):
    current_frequency = 0
    for frequency in map(int, inputs):
        current_frequency += frequency
    return current_frequency

def first_frequency_reached_twice(inputs):
    frequency_history = set([0])
    current_frequency = 0
    frequency_reached_twice = None
    while frequency_reached_twice == None:
        for frequency in map(int, inputs):
            current_frequency += frequency
            if current_frequency in frequency_history:
                frequency_reached_twice = current_frequency
                break
            else:
                frequency_history.add(current_frequency)
    return frequency_reached_twice

# Day Two Solutions
def box_checksum(inputs):
    twos = 0
    threes = 0
    for box_id in inputs:
        chars = defaultdict(int)
        for char in box_id:
            chars[char] += 1
        if 2 in chars.values():
            twos += 1
        if 3 in chars.values():
            threes += 1
    return twos * threes

def compare_box_ids(box1, box2):
    diffs = [x for x in zip(box1, box2) if x[0] != x[1]]
    return len(diffs) == 1

def find_correct_boxes(inputs):
    for box1 in inputs:
        for box2 in inputs:
            if box1 != box2 and compare_box_ids(box1, box2):
                return ''.join([x for i,x in enumerate(box1) if x == box2[i]])
    return "No correct boxes found."

# Day Three Solutions
def find_overlapping_claims(inputs):
    input_regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    fabric = [[0] * 1000 for i in range(1000)]
    for line in inputs:
        match = re.search(input_regex, line)
        (ident, x, y, w, h) = map(int, match.groups())
        for i in range(x, x+w):
            for j in range(y, y+h):
                fabric[i][j] += 1
    overlapping_regions = 0
    for column in fabric:
        for region in column:
            if region >= 2:
                overlapping_regions += 1
    return overlapping_regions

def find_non_overlapping_claim(inputs):
    input_regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    fabric = [[0] * 1000 for i in range(1000)]
    idents = {}
    for line in inputs:
        match = re.search(input_regex, line)
        (ident, x, y, w, h) = map(int, match.groups())
        idents[ident] = w*h
        for i in range(x, x+w):
            for j in range(y, y+h):
                if fabric[i][j] == 0:
                    fabric[i][j] = ident
                else:
                    fabric[i][j] = -1
    for ident in idents.keys():
        matches = len([i for i in list(chain.from_iterable(fabric)) if i == ident])
        if matches == idents[ident]:
            return ident
    return "No non-overlapping claim found."

def resolve_polymer(inputs):
    polymer = inputs[0]
    regex = re.compile(r'Aa|Bb|Cc|Dd|Ee|Ff|Gg|Hh|Ii|Jj|Kk|Ll|Mm|Nn|Oo|Pp|Qq|Rr|Ss|Tt|Uu|Vv|Ww|Xx|Yy|Zz|aA|bB|cC|dD|eE|fF|gG|hH|iI|jJ|kK|lL|mM|nN|oO|pP|qQ|rR|sS|tT|uU|vV|wW|xX|yY|zZ')
    next_polymer = re.sub(regex, '', polymer)
    while(polymer != next_polymer):
        polymer = next_polymer
        next_polymer = re.sub(regex, '', polymer)
    return len(polymer)

def find_shortest_polymer(inputs):
    starting_polymer = inputs[0]
    shortest_polymer_len = 1000000
    for char in 'abcdefghijklmnopqrstuvwxyz':
        print(char)
        polymer = starting_polymer
        regex = re.compile(char+'|'+char.upper())
        next_polymer = re.sub(regex, '', polymer)
        while(polymer != next_polymer):
            polymer = next_polymer
            next_polymer = re.sub(regex, '', polymer)
        print(len(starting_polymer), len(polymer))
        resolved_polymer_len = resolve_polymer([polymer])
        print(resolved_polymer_len)
        if resolved_polymer_len < shortest_polymer_len:
            shortest_polymer_len = resolved_polymer_len
    return shortest_polymer_len

def largest_area_of_isolation(inputs):
    points = [tuple(map(int, line.split(', '))) for line in inputs]
    min_x = min([point[0] for point in points])
    max_x = max([point[0] for point in points])
    min_y = min([point[1] for point in points])
    max_y = max([point[1] for point in points])
    closest_points = defaultdict(int)
    infinite_points = set()
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            coord = (x, y)
            distances = {}
            for point in points:
                distances[point] = manhattan_distance(coord, point)
            if len([v for v in distances.values() if v == min(distances.values())]) > 1:
                continue
            closest_point = min(distances, key=distances.get)
            if x in [min_x, max_x] or y in [min_y, max_y]:
                infinite_points.add(closest_point)
            closest_points[closest_point] += 1
    return max([closest_points[k] for k in closest_points.keys() if k not in infinite_points])

solution_list = [
    [sum_frequencies, first_frequency_reached_twice],
    [box_checksum, find_correct_boxes],
    [find_overlapping_claims, find_non_overlapping_claim],
    ['',''],
    [resolve_polymer, find_shortest_polymer],
    [largest_area_of_isolation]
]

def get_solver(day, part):
    return solution_list[int(day)-1][int(part)-1]

