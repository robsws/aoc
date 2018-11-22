import sys
from math import floor

input_filename = sys.argv[1]
priming_iterations = int(sys.argv[2])
file = open(input_filename,'r')

grid = [list(x) for x in file.read().splitlines()]

turn_left  = {'n': 'w', 'e': 'n', 's': 'e', 'w': 's'}
turn_right = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
go_forward = {
    'n': lambda p: {'x':p['x'], 'y':p['y']-1},
    'e': lambda p: {'x':p['x']+1, 'y':p['y']},
    's': lambda p: {'x':p['x'], 'y':p['y']+1},
    'w': lambda p: {'x':p['x']-1, 'y':p['y']}
}

carrier_position = {'x':floor(len(grid[0])/2), 'y':floor(len(grid)/2)}
carrier_direction = 'n'

def print_grid(pos,dire):
    for y, row in enumerate(grid):
        row_str = ''
        for x, cell in enumerate(row):
            if pos['x'] == x and pos['y'] == y:
                if cell == '.':
                    row_str += dire.lower()
                else:
                    row_str += dire.upper()
            else:
                row_str += cell
        print(row_str)

def add_column_left():
    global carrier_position
    global grid
    for row in grid:
        row.insert(0, '.')
    carrier_position['x'] += 1

def add_column_right():
    global grid
    for row in grid:
        row.append('.')

def add_row_top():
    global carrier_position
    global grid
    grid.insert(0, ['.'] * len(grid[0]))
    carrier_position['y'] += 1

def add_row_bottom():
    global grid
    grid.append(['.'] * len(grid[0]))

def burst():
    global carrier_position
    global carrier_direction
    if carrier_position['x'] < 0:
        add_column_left()
    elif carrier_position['x'] >= len(grid[0]):
        add_column_right()
    elif carrier_position['y'] < 0:
        add_row_top()
    elif carrier_position['y'] >= len(grid):
        add_row_bottom()
    infected = False
    if grid[carrier_position['y']][carrier_position['x']] == '#':
        carrier_direction = turn_right[carrier_direction]
        grid[carrier_position['y']][carrier_position['x']] = '.'
    else:
        carrier_direction = turn_left[carrier_direction]
        grid[carrier_position['y']][carrier_position['x']] = '#'
        infected = True
    carrier_position = go_forward[carrier_direction](carrier_position)
    return infected

amount_infected = 0
for i in range(priming_iterations):
    if burst():
        amount_infected += 1
print(amount_infected)
