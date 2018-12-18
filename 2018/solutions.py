from utils import *
from collections import defaultdict
from itertools import chain
from time import sleep
from copy import deepcopy
from enum import Enum
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

# Day Nine Solutions
def winning_elfs_score(inputs, multiplier=1):
    regex = re.compile(r'(\d+) players; last marble is worth (\d+) points')
    (amount_of_players, last_marble) = map(int, re.match(regex, inputs[0]).groups())
    last_marble *= multiplier
    players = defaultdict(int)
    circle = CircularList([0])
    current_marble = 0
    next_marble = 1
    while(next_marble <= last_marble):
        current_player = current_marble % amount_of_players
        if next_marble % 23 == 0:
            players[current_player] += next_marble
            current_pos = circle.find(current_marble)
            current_marble = circle.get(current_pos - 6)
            players[current_player] += circle.get(current_pos - 7)
            # print(next_marble, circle.get(current_pos - 7), next_marble + circle.get(current_pos - 7), current_marble)
            circle.remove(circle.get(current_pos - 7))
        else:
            circle.add(next_marble, circle.find(current_marble)+2)
            current_marble = next_marble
        next_marble += 1
        print(circle)
    return max(players.values())

def winning_elfs_score_times_hundred(inputs):
    return winning_elfs_score(inputs, 100)

# Day Ten Solutions
class Star:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

def print_stars(stars, i):
    positions = [star.pos for star in stars]
    minx = min([p[0] for p in positions])
    miny = min([p[1] for p in positions])
    offset = (abs(minx),abs(miny))
    offset_positions = [(p[0]+offset[0],p[1]+offset[1]) for p in positions]
    maxx = max([p[0] for p in offset_positions])+1
    maxy = max([p[1] for p in offset_positions])+1
    closeness = sum([manhattan_distance(offset_positions[0], p) for p in offset_positions])
    # print(closeness)
    if(closeness < 8000):
        print(i)
        for y in range(maxy):
            line = ''
            for x in range(maxx):
                if (x, y) in offset_positions:
                    line += '#'
                else:
                    line += '.'
            print(line)
        print()

def display_star_message(inputs):
    regex = re.compile(r'^position=<\s*([-+]?\d+),\s*([-+]?\d+)>\s*velocity=<\s*([-+]?\d+),\s*([-+]?\d+)>')
    stars = []
    for line in inputs:
        (posx, posy, velx, vely) = map(int, re.match(regex, line).groups())
        stars.append(Star([posx, posy],[velx, vely]))
    for i in range(50000):
        if(i % 1000 == 0):
            print(i)
        print_stars(stars, i)
        for star in stars:
            star.move()
        # sleep(1)
    return 0

# Day Eleven Solutions
def fuel_cell_power_level(x, y, serial_no):
    rack_id = x + 10
    power_level = (rack_id * y + serial_no) * rack_id
    return int(power_level/100) - int(power_level/1000)*10 - 5

def largest_power_cluster_of_three(inputs):
    serial_no = int(inputs[0])
    grid = [[fuel_cell_power_level(x, y, serial_no) for x in range(300)] for y in range(300)]
    highest_total = -10000
    highest_total_pos = (-1, -1)
    for x in range(300 - 3):
        for y in range(300 - 3):
            total = sum([sum(rack[x:x+3]) for rack in grid[y:y+3]])
            if(total > highest_total):
                highest_total = total
                highest_total_pos = (x, y)
    return highest_total_pos

def largest_power_cluster(inputs):
    serial_no = int(inputs[0])
    grid = [[fuel_cell_power_level(x, y, serial_no) for x in range(300)] for y in range(300)]
    highest_total = -1000000
    highest_total_pos = (-1, -1, -1)
    for s in range(300):
        print(s)
        for x in range(300 - s):
            for y in range(300 - s):
                total = sum([sum(rack[x:x+s]) for rack in grid[y:y+s]])
                if(total > highest_total):
                    highest_total = total
                    highest_total_pos = (x, y, s)
                    print(highest_total, highest_total_pos)
    return highest_total_pos

# Day Twelve Solutions
def sum_of_pot_ids_with_plants(inputs):
    extra_pots_either_side = 30
    first_line_regex = re.compile(r'initial state: ([#\.]+)')
    rule_regex = re.compile(r'([#\.]{5}) => ([#\.])')
    state = ['.']*extra_pots_either_side + list(re.match(first_line_regex, inputs.pop(0)).groups()[0]) + ['.']*extra_pots_either_side
    inputs.pop(0)
    rules = dict()
    for line in inputs:
        (state_str, output) = re.match(rule_regex, line).groups()
        rules[tuple(state_str)] = output
    for i in range(20):
        next_state = ['.']*len(state)
        for pot in range(2, len(state)-1):
            neighbourhood = tuple(state[pot-2:pot+3])
            if neighbourhood not in rules:
                next_state[pot] = '.'
            else:
                next_state[pot] = rules[tuple(state[pot-2:pot+3])]
        state = next_state
    return sum([i-50 for i, pot in enumerate(state) if pot == '#'])

def sum_of_pot_ids_with_plants_at_end_of_time(inputs):
    # after a certain number of iterations (about 117), the pattern repeats the same every time
    # except offset by one each time.
    # the offset is current iteration minus 48
    repeating_pattern = '#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#..##.#'
    total = 0
    fifty_billion = 50000000000
    for i, j in enumerate(range(fifty_billion-48, fifty_billion-48+len(repeating_pattern))):
        if repeating_pattern[i] == '#':
            total += j
    print(total)

# Day Thirteen Solutions
dir_map = {
    '^': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
}

turn_right = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (-1, 0): (0, -1),
    (0, 1): (-1, 0),
}

turn_left = {
    (0, -1): (-1, 0),
    (1, 0): (0, -1),
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
}

cart_turn_seq = [
    lambda x: turn_left[x],
    lambda x: x,
    lambda x: turn_right[x]
]

def first_collision_location(inputs):
    # Gather information from input
    grid = []
    for line in inputs:
        grid.append(list(line))
    carts = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in dir_map:
                carts.append({'x':x, 'y':y, 'dir':dir_map[grid[y][x]], 'turns':0, 'id':len(carts)})
                grid[y][x] = '|'
    # Run the simulation
    collision_location = (-1, -1)
    while collision_location == (-1, -1):
        for cart in carts:
            (next_x, next_y) = vadd((cart['x'], cart['y']), cart['dir'])
            cart['x'] = next_x
            cart['y'] = next_y
            # Check for collision
            for other_cart in carts:
                if cart['x'] == other_cart['x'] and cart['y'] == other_cart['y'] and cart['id'] != other_cart['id']:
                    collision_location = (next_x, next_y)
                    break
            # Turn 90 degrees if at a curve
            if grid[next_y][next_x] == '\\':
                if cart['dir'][0] != 0:
                    cart['dir'] = turn_right[cart['dir']]
                else:
                    cart['dir'] = turn_left[cart['dir']]
            elif grid[next_y][next_x] == '/':
                if cart['dir'][0] != 0:
                    cart['dir'] = turn_left[cart['dir']]
                else:
                    cart['dir'] = turn_right[cart['dir']]
            # Turn next direction in sequence at intersection
            elif grid[next_y][next_x] == '+':
                cart['dir'] = cart_turn_seq[cart['turns']%len(cart_turn_seq)](cart['dir'])
                cart['turns'] += 1
    return collision_location

def last_cart_standing(inputs):
    # Gather information from input
    grid = []
    for line in inputs:
        grid.append(list(line))
    carts = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in dir_map:
                carts.append({'x':x, 'y':y, 'dir':dir_map[grid[y][x]], 'turns':0, 'id':len(carts)})
                grid[y][x] = '|'
    # Run the simulation
    collision_location = (-1, -1)
    while len(carts) > 1:
        carts.sort(key=lambda cart: (cart['y'],cart['x']))
        to_remove = []
        for cart in carts:
            (next_x, next_y) = vadd((cart['x'], cart['y']), cart['dir'])
            cart['x'] = next_x
            cart['y'] = next_y
            # Check for collision
            for other_cart in [c for c in carts if c not in to_remove]:
                if cart['x'] == other_cart['x'] and cart['y'] == other_cart['y'] and cart['id'] != other_cart['id']:
                    to_remove.append(cart)
                    to_remove.append(other_cart)
            # Turn 90 degrees if at a curve
            if grid[next_y][next_x] == '\\':
                if cart['dir'][0] != 0:
                    cart['dir'] = turn_right[cart['dir']]
                else:
                    cart['dir'] = turn_left[cart['dir']]
            elif grid[next_y][next_x] == '/':
                if cart['dir'][0] != 0:
                    cart['dir'] = turn_left[cart['dir']]
                else:
                    cart['dir'] = turn_right[cart['dir']]
            # Turn next direction in sequence at intersection
            elif grid[next_y][next_x] == '+':
                cart['dir'] = cart_turn_seq[cart['turns']%len(cart_turn_seq)](cart['dir'])
                cart['turns'] += 1
        for cart in to_remove:
            carts.remove(cart)
    return (carts[0]['x'], carts[0]['y'])

# Day Fourteen Solutions
def recipe_scores_after_n(inputs):
    n = int(inputs[0])
    scores = [3, 7]
    elves = [0, 1]
    while len(scores) < n + 10:
        # print('scores', scores)
        # print('elves', elves)
        total = scores[elves[0]] + scores[elves[1]]
        tens = int(total/10)
        units = total - tens*10
        if tens != 0:
            scores.append(tens)
        scores.append(units)
        for e in range(len(elves)):
            elves[e] = (elves[e] + scores[elves[e]] + 1) % len(scores)
    return ''.join(map(str, scores[n:n+10]))

def recipe_scores_before_sequence(inputs):
    seq = list(map(int, list(inputs[0])))
    scores = [3, 7]
    elves = [0, 1]
    recipes_to_left = 0
    while recipes_to_left == 0:
        total = scores[elves[0]] + scores[elves[1]]
        tens = int(total/10)
        units = total - tens*10
        if tens != 0:
            scores.append(tens)
            if scores[-len(seq):] == seq:
                recipes_to_left = len(scores) - len(seq)
                break
        scores.append(units)
        if scores[-len(seq):] == seq:
            recipes_to_left = len(scores) - len(seq)
            break
        for e in range(len(elves)):
            elves[e] = (elves[e] + scores[elves[e]] + 1) % len(scores)
    return recipes_to_left


# Day Fifteen Solutions
class UnitType(Enum):
    ELF = 1
    GOBLIN = 2

class Unit:
    def __init__(self, hp=200, ap=3, kind=UnitType.ELF):
        self.hp = hp
        self.ap = ap
        self.kind = kind
    def __str__(self):
        if self.kind == UnitType.ELF:
            return 'E'
        else:
            return 'G'

class Tile(Enum):
    SPACE = 1
    WALL = 2

tile_chars = {
    '.': Tile.SPACE,
    '#': Tile.WALL,
    'G': Tile.SPACE,
    'E': Tile.SPACE
}

def simulate_round(static_grid, dynamic_grid):
    for y in range(len(dynamic_grid)):
        for x in range(len(dynamic_grid[0])):
            if dynamic_grid[y][x] is not None:
                print('')

def get_conflict_outcome(inputs):
    # Load the grid into memory
    static_grid = []
    dynamic_grid = [[None] * len(inputs[0]) for i in range(len(inputs))]
    for y, line in enumerate(inputs):
        row = list(line)
        static_grid.append(list(map(lambda x: tile_chars[x], row)))
        for x, char in enumerate(row):
            if char == 'G':
                dynamic_grid[y][x] = Unit(kind=UnitType.GOBLIN)
            elif char == 'E':
                dynamic_grid[y][x] = Unit(kind=UnitType.ELF)
    # Simulate rounds
    i = 0
    (dynamic_grid, ended) = simulate_round(static_grid, dynamic_grid)
    while not ended:
        (dynamic_grid, ended) = simulate_round(static_grid, dynamic_grid)
        i += 1
    # Calculate outcome
    hp_left = sum([unit.hp for unit in chain.from_iterable(dynamic_grid) if unit is not None])
    return i * hp_left

# Day Sixteen Solutions
operations = {
    12: lambda r,a,b: r[a] + r[b],              #addr
     2: lambda r,a,b: r[a] + b,                 #addi
    14: lambda r,a,b: r[a] * r[b],              #mulr
     0: lambda r,a,b: r[a] * b,                 #muli
    15: lambda r,a,b: r[a] & r[b],              #banr
     1: lambda r,a,b: r[a] & b,                 #bani
    11: lambda r,a,b: r[a] | r[b],              #borr
     7: lambda r,a,b: r[a] | b,                 #bori
     6: lambda r,a,b: r[a],                     #setr
     3: lambda r,a,b: a,                        #seti
    10: lambda r,a,b: 1 if a > r[b] else 0,     #gtir
     8: lambda r,a,b: 1 if r[a] > b else 0,     #gtri
    13: lambda r,a,b: 1 if r[a] > r[b] else 0,  #gtrr
     5: lambda r,a,b: 1 if a == r[b] else 0,    #eqir
     9: lambda r,a,b: 1 if r[a] == b else 0,    #eqri
     4: lambda r,a,b: 1 if r[a] == r[b] else 0, #eqrr
}

def samples_fit_three_or_more_opcodes(inputs):
    sample_before_regex = re.compile(r'Before: \[(\d+), (\d+), (\d+), (\d+)\]')
    sample_command_regex = re.compile(r'(\d+) (\d+) (\d+) (\d+)')
    sample_after_regex = re.compile(r'After:  \[(\d+), (\d+), (\d+), (\d+)\]')
    i = 0
    total = 0
    while i < len(inputs):
        if not re.match(sample_before_regex, inputs[i]):
            break
        state_before = list(map(int, re.match(sample_before_regex, inputs[i]).groups()))
        command = list(map(int, re.match(sample_command_regex, inputs[i+1]).groups()))
        state_after = list(map(int, re.match(sample_after_regex, inputs[i+2]).groups()))
        possible_ops = 0
        for op in operations:
            state = deepcopy(state_before)
            state[command[3]] = operations[op](state,command[1],command[2])
            if state == state_after:
                possible_ops += 1
        if possible_ops >= 3:
            total += 1
        i += 4
    return total

def run_test_program(inputs):
    sample_command_regex = re.compile(r'(\d+) (\d+) (\d+) (\d+)')
    start = [i for i in range(len(inputs)) if inputs[i:i+3] == ['','','']][0] + 3
    registers = [0,0,0,0]
    for i in range(start, len(inputs)):
        (opcode, input_a, input_b, output) = list(map(int, re.match(sample_command_regex, inputs[i]).groups()))
        registers[output] = operations[opcode](registers, input_a, input_b)
    return(registers[0])

# Day Seventeen Solutions
def amount_of_wet_sand(inputs):
    v_regex = re.compile(r'x=(\d+), y=(\d+)..(\d+)')
    h_regex = re.compile(r'y=(\d+), x=(\d+)..(\d+)')
    v_lines = []
    h_lines = []
    for line in inputs:
        if re.match(v_regex, line):
            v_lines.append(list(map(int, re.match(v_regex, line).groups())))
        elif re.match(h_regex, line):
            h_lines.append(list(map(int, re.match(h_regex, line).groups())))
        else:
            print('invalid rule')

# Day Eighteen Solutions
def get_surrounding_elements(grid, x, y):
    elements = []
    if y > 0:
        # top row
        if x > 0:
            # left column
            elements.append(grid[y-1][x-1])
        if x < len(grid[0])-1:
            # right column
            elements.append(grid[y-1][x+1])
        # middle column
        elements.append(grid[y-1][x])
    if y < len(grid)-1:
        # bottom row
        if x > 0:
            # left column
            elements.append(grid[y+1][x-1])
        if x < len(grid[0])-1:
            # right column
            elements.append(grid[y+1][x+1])
        # middle column
        elements.append(grid[y+1][x])
    # middle row
    if x > 0:
        # left column
        elements.append(grid[y][x-1])
    if x < len(grid[0])-1:
        # right column
        elements.append(grid[y][x+1])
    return elements

def print_iteration_info(i, grid):
    # print(i,'-')
    # print_grid(grid)
    number_of_trees = sum([1 for acre in chain.from_iterable(grid) if acre == '|'])
    number_of_lumber = sum([1 for acre in chain.from_iterable(grid) if acre == '#'])
    print(i, number_of_lumber * number_of_trees)
    # print()

def total_resource_value(inputs, iterations=10):
    grid = []
    for line in inputs:
        grid.append(list(line))
    print_iteration_info(0, grid)
    for i in range(iterations):
        next_grid = deepcopy(grid)
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                surrounding = get_surrounding_elements(grid, x, y)
                amount_of_trees = sum([1 for acre in surrounding if acre == '|'])
                amount_of_lumber = sum([1 for acre in surrounding if acre == '#'])
                if grid[y][x] == '.' and amount_of_trees >= 3:
                    next_grid[y][x] = '|'
                elif grid[y][x] == '|' and amount_of_lumber >= 3:
                    next_grid[y][x] = '#'
                elif grid[y][x] == '#' and (amount_of_trees == 0 or amount_of_lumber == 0):
                    next_grid[y][x] = '.'
        grid = next_grid
        print_iteration_info(i, grid)

    # Calculate resource value
    number_of_trees = sum([1 for acre in chain.from_iterable(grid) if acre == '|'])
    number_of_lumber = sum([1 for acre in chain.from_iterable(grid) if acre == '#'])
    return number_of_lumber * number_of_trees

def total_resource_value_after_one_billion(inputs):
    return total_resource_value(inputs, iterations=1000000000)
    # Observed loop after 416 iterations and calculated value for iteration 1 billion

solution_list = [
    [sum_frequencies, first_frequency_reached_twice],
    [box_checksum, find_correct_boxes],
    [find_overlapping_claims, find_non_overlapping_claim],
    [safest_minute_strat_one, safest_minute_strat_two],
    [resolve_polymer, find_shortest_polymer],
    [largest_area_of_isolation, area_close_to_coords],
    [order_steps, time_to_construct_sleigh],
    [sum_all_tree_metadata, calculate_tree_value],
    [winning_elfs_score, winning_elfs_score_times_hundred],
    [display_star_message, display_star_message],
    [largest_power_cluster_of_three, largest_power_cluster],
    [sum_of_pot_ids_with_plants, sum_of_pot_ids_with_plants_at_end_of_time],
    [first_collision_location, last_cart_standing],
    [recipe_scores_after_n, recipe_scores_before_sequence],
    [get_conflict_outcome],
    [samples_fit_three_or_more_opcodes, run_test_program],
    [amount_of_wet_sand],
    [total_resource_value, total_resource_value_after_one_billion]
]

def get_solver(day, part):
    return solution_list[int(day)-1][int(part)-1]

