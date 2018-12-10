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

# Day Four Solutions
def parse_guard_log(inputs):
    inputs.sort()
    input_regex = re.compile(r'\[([\d-]+) \d+:(\d+)\] (?:Guard #(\d+) begins shift|(falls asleep)|(wakes up))')
    date_guards = dict()
    minutes_asleep = defaultdict(set)
    current_guard = -1
    current_date = -1
    for line in inputs:
        (date, time, ident, asleep, wakes) = re.match(input_regex, line).groups()
        if ident is not None:
            # New shift
            current_guard = int(ident)
        elif asleep is not None:
            date_guards[date] = current_guard
            time_fell_asleep = int(time)
        elif wakes is not None:
            time_woken = int(time)
            for t in range(time_fell_asleep, time_woken+1):
                minutes_asleep[date].add(t)
    for date in sorted(date_guards.keys()):
        print(date,date_guards[date],minutes_asleep[date])
    return (date_guards, minutes_asleep)

def safest_minute_strat_one(inputs):
    (date_guards, minutes_asleep) = parse_guard_log(inputs)
    guard_total = defaultdict(int)
    for date in date_guards.keys():
        guard_total[date_guards[date]] += len(minutes_asleep[date])
    sleepiest_guard = max(guard_total, key=guard_total.get)
    guard_minute_totals = [0]*60
    for minute in range(0, 60):
        guard_minute_totals[minute] = sum([1 for d in [date for date in date_guards.keys() if date_guards[date] == sleepiest_guard] if minute in minutes_asleep[d]])
    most_asleep = max(guard_minute_totals)
    sleepiest_minute = guard_minute_totals.index(most_asleep)
    return sleepiest_minute * sleepiest_guard

def safest_minute_strat_two(inputs):
    (date_guards, minutes_asleep) = parse_guard_log(inputs)
    most_asleep = 0
    sleepiest_minute = -1
    sleepiest_guard = -1
    for guard in sorted(list(set(date_guards.values()))):
        print(guard, len([date for date in date_guards.keys() if date_guards[date] == guard]))
        for minute in range(0, 60):
            total_asleep = sum([1 for d in [date for date in date_guards.keys() if date_guards[date] == guard] if minute in minutes_asleep[d]])
            if total_asleep > most_asleep:
                most_asleep = total_asleep
                sleepiest_minute = minute
                sleepiest_guard = guard
    print(sleepiest_guard, sleepiest_minute, most_asleep)
    return sleepiest_minute * sleepiest_guard

# Day Five Solutions
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

# Day Six Solutions
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

def area_close_to_coords(inputs):
    points = [tuple(map(int, line.split(', '))) for line in inputs]
    min_x = min([point[0] for point in points])
    max_x = max([point[0] for point in points])
    min_y = min([point[1] for point in points])
    max_y = max([point[1] for point in points])
    area_size = 0
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            coord = (x, y)
            distance_sum = sum([manhattan_distance(coord, point) for point in points])
            if distance_sum < 10000:
                area_size += 1
    return area_size

# Day Seven Solutions
def order_steps(inputs):
    regex = re.compile(r'Step (\w) must be finished before step (\w) can begin.')
    next_steps = defaultdict(list)
    dependencies = defaultdict(list)
    for line in inputs:
        (step, next_step) = re.match(regex, line).groups()
        dependencies[next_step].append(step)
        next_steps[step].append(next_step)
    available_steps = [s for s in next_steps if s not in chain.from_iterable(next_steps.values())]
    steps_str = ''
    while len(available_steps) > 0:
        available_steps.sort(reverse=True)
        step = available_steps.pop()
        steps_str += step
        possible_next_steps = next_steps[step]
        for next_step in possible_next_steps:
            dependencies[next_step].remove(step)
            if len(dependencies[next_step]) == 0:
                available_steps.append(next_step)
    return steps_str

def time_to_construct_sleigh(inputs):
    regex = re.compile(r'Step (\w) must be finished before step (\w) can begin.')
    next_steps = defaultdict(list)
    dependencies = defaultdict(list)
    for line in inputs:
        (step, next_step) = re.match(regex, line).groups()
        dependencies[next_step].append(step)
        next_steps[step].append(next_step)
    available_steps = [s for s in next_steps if s not in chain.from_iterable(next_steps.values())]
    t = 0
    available_workers = 5
    step_timers = dict()
    while len(available_steps) > 0 or len(step_timers) > 0:
        for step in step_timers:
            step_timers[step] -= 1
            if step_timers[step] == 0:
                available_workers += 1
                possible_next_steps = next_steps[step]
                for next_step in possible_next_steps:
                    dependencies[next_step].remove(step)
                    if len(dependencies[next_step]) == 0:
                        available_steps.append(next_step)
        for step in [s for s in step_timers if step_timers[s] == 0]:
            del step_timers[step]
        while available_workers > 0 and len(available_steps) > 0:
            available_steps.sort(reverse=True)
            step = available_steps.pop()
            step_timers[step] = ord(step) - 4
            available_workers -= 1
        t += 1
    return t-1

# Day Eight Solutions
def sum_tree_metadata(tree, pointer):
    number_of_children = tree[pointer]
    number_of_metadata = tree[pointer+1]
    metadata_sum = 0
    pointer += 2
    for i in range(number_of_children):
        (subtree_metadata_sum, pointer) = sum_tree_metadata(tree, pointer)
        metadata_sum += subtree_metadata_sum
    for i in range(number_of_metadata):
        metadata_sum += tree[pointer]
        pointer += 1
    return (metadata_sum, pointer)

def sum_all_tree_metadata(inputs):
    number_list = list(map(int, inputs[0].split(' ')))
    return sum_tree_metadata(number_list, 0)[0]

def calculate_node_value(tree, pointer):
    number_of_children = tree[pointer]
    number_of_metadata = tree[pointer+1]
    metadata_sum = 0
    pointer += 2
    subtree_values = dict()
    value = 0
    for i in range(number_of_children):
        (subtree_value, pointer) = calculate_node_value(tree, pointer)
        subtree_values[i+1] = subtree_value
    for i in range(number_of_metadata):
        if number_of_children == 0:
            value += tree[pointer]
        elif tree[pointer] in subtree_values:
            value += subtree_values[tree[pointer]]
        pointer += 1
    return (value, pointer)

def calculate_tree_value(inputs):
    number_list = list(map(int, inputs[0].split(' ')))
    return calculate_node_value(number_list, 0)[0]

solution_list = [
    [sum_frequencies, first_frequency_reached_twice],
    [box_checksum, find_correct_boxes],
    [find_overlapping_claims, find_non_overlapping_claim],
    [safest_minute_strat_one, safest_minute_strat_two],
    [resolve_polymer, find_shortest_polymer],
    [largest_area_of_isolation, area_close_to_coords],
    [order_steps, time_to_construct_sleigh],
    [sum_all_tree_metadata, calculate_tree_value]
]

def get_solver(day, part):
    return solution_list[int(day)-1][int(part)-1]

