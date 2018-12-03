def print_grid(grid):
    print(grid)
    for row in grid:
        print(''.join(map(str, row)))