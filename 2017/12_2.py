import sys
import time

input_filename = sys.argv[1]
file = open(input_filename,'r')

graph = dict()

for line in file.read().splitlines():
    (ident, connected_str) = line.split(' <-> ')
    connected = set(map(int, connected_str.split(', ')))
    graph[int(ident)] = connected

groups = 0
while len(graph) > 0:
    ids_to_check = {list(graph.keys())[0]}
    checked = set()
    while len(ids_to_check) > 0:
        for ident in ids_to_check:
            ids_to_check = ids_to_check.union(graph[ident]).difference(checked)
            ids_to_check.remove(ident)
            checked.add(ident)
    groups += 1
    for ident in checked:
        graph.pop(ident)

print('part 2: '+str(groups))