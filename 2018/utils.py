import os

def print_grid(grid):
    for row in grid:
        print(''.join(map(str, row)))

def manhattan_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

class CircularList:
    def __init__(self):
        self.l = list()

    def __init__(self, initlist):
        self.l = initlist

    def __str__(self):
        return str(self.l)

    def find(self, elem):
        return self.l.index(elem)

    def add(self, elem, pos):
        pos = pos % len(self.l)
        self.l.insert(pos, elem)

    def remove(self, elem):
        return self.l.remove(elem)

    def get(self, pos):
        return self.l[pos % len(self.l)]

def vadd(vec1, vec2):
    return (sum(x) for x in zip(vec1, vec2))