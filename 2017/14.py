import sys
from knot_hash import knot_hash

salt = sys.argv[1]
used_count = 0

def int_to_bin(num):
    binary = ''
    n = 3
    while num > 0 and n >= 0:
        if num - (2 ** n) >= 0:
            num = num - (2 ** n)
            binary += '1'
        else:
            binary += '0'
        n -= 1
    while len(binary) < 4:
        binary += '0'
    return binary

grid = []

def purge_region(coord):
    grid[coord[0]][coord[1]] = '0'
    squares_to_check_next = [
        (coord[0],coord[1]-1),
        (coord[0],coord[1]+1),
        (coord[0]-1,coord[1]),
        (coord[0]+1,coord[1])
    ]
    for square in squares_to_check_next:
        if square[1] >= 0 and square[1] < len(grid) and square[0] >= 0 and square[0] < len(grid[0]) and grid[square[0]][square[1]] == '1':
            purge_region(square)

for i in range(128):
    plaintext = salt+'-'+str(i)
    hashtext = knot_hash(plaintext)
    binary = ''.join([str(int_to_bin(int(c, 16))) for c in hashtext])
    used_count += binary.count('1')
    grid.append(list(binary))

regions = 0
for x in range(128):
    for y in range(128):
        if grid[x][y] == '1':
            purge_region((x, y))
            regions += 1
            print(regions)

print('part 1: '+str(used_count))
print('part 2: '+str(regions))