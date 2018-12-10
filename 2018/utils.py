def print_grid(grid):
    print(grid)
    for row in grid:
        print(''.join(map(str, row)))

def manhattan_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])   