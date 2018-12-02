import utils
from collections import defaultdict

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

solution_list = [
    [sum_frequencies, first_frequency_reached_twice],
    [box_checksum, find_correct_boxes]
]

def get_solver(day, part):
    return solution_list[int(day)-1][int(part)-1]

