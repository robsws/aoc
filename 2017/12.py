import sys
import time

input_filename = sys.argv[1]
file = open(input_filename,'r')

graph = dict()

for line in file.read().splitlines():
    (ident, connected_str) = line.split(' <-> ')
    connected = set(map(int, connected_str.split(', ')))
    graph[int(ident)] = connected


ids_to_check = {list(graph.keys())[0]}
checked = set()
while len(ids_to_check) > 0:
    for ident in ids_to_check:
        ids_to_check = ids_to_check.union(graph[ident]).difference(checked)
        ids_to_check.remove(ident)
        checked.add(ident)

print('part 1: '+str(len(checked)))