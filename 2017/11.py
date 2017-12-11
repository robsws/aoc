import sys

input_filename = sys.argv[1]
file = open(input_filename,'r')

# Coordinate system is aligned with x=ne and y=n
# Meaning that se and nw are effectively diagonal moves
directions = {
    'n':  [0, 1],
    'ne': [1, 0],
    'se': [1, -1],
    's':  [0, -1],
    'sw': [-1, 0],
    'nw': [-1, 1]
}

def vector_add(a, b):
    return [sum(x) for x in zip(a, b)]

def shortest_route_length_back(position):
    shortest_length = 0    
    # Upper right or lower left quadrants are just manhattan distance as our coordinates are aligned that way
    if (position[0] > 0 and position[1] > 0) or (position[0] < 0 and position[1] < 0):
        shortest_length = abs(position[0]) + abs(position[1])
    # For upper left quadrant we have to go se then s, which is the same as the amount of steps n we are
    elif position[0] < 0:
        shortest_length = position[1]
    # For lower right quadrant we have to go nw then sw, which is the same as the amount of steps ne we are
    elif position[1] < 0:
        shortest_length = position[0]
    return shortest_length

position = [0, 0]
furthest_away_from_home = 0

for direction in file.read().rstrip().split(','):
    position = vector_add(position, directions[direction])
    distance = shortest_route_length_back(position)
    if distance > furthest_away_from_home:
        furthest_away_from_home = distance

print('part 1: '+str(shortest_route_length_back(position)))
print('part 2: '+str(furthest_away_from_home))
