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


solution_list = [
    [sum_frequencies, first_frequency_reached_twice],
    [box_checksum, find_correct_boxes],
    [find_overlapping_claims, find_non_overlapping_claim],
    [safest_minute_strat_one, safest_minute_strat_two]
]

def get_solver(day, part):
    return solution_list[int(day)-1][int(part)-1]

