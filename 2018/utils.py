def print_grid(grid):
    print(grid)
    for row in grid:
        print(''.join(map(str, row)))

def manhattan_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

class CircularList:
    def __init__(self):
        self.l = list()
        self.pos = dict()

    def __init__(self, initlist):
        self.l = initlist
        self.pos = dict()
        for i, elem in enumerate(self.l):
            self.pos[elem] = i

    def __str__(self):
        return str(self.l)

    def find(self, elem):
        return self.pos[elem]

    def add(self, elem, pos):
        pos = pos % len(self.l)
        self.l.insert(pos, elem)
        self.pos[elem] = pos
        for i in range(pos, len(self.l)):
            self.pos[self.l[i]] = (self.pos[self.l[i]] + 1) % len(self.l)

    def remove(self, elem):
        for i in range(self.pos[elem], len(self.l)):
            self.pos[self.l[i]] = self.pos[self.l[i]] - 1
        return self.l.remove(elem)

    def get(self, pos):
        return self.l[pos % len(self.l)]


