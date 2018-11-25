import sys
from math import floor
from collections import defaultdict
from copy import deepcopy

input_filename = sys.argv[1]
file = open(input_filename,'r')
components = [tuple(map(int, x.split('/'))) for x in file.read().splitlines()]

# get all combinations of pairs of components
combos = defaultdict(set)
for component in components:
    for other_component in components:
        if component != other_component:
            for port in component:
                if port in other_component:
                    combos[component].add(other_component)

best_so_far = ((), 0)

def search_combos(component, port, components_left):
    global best_so_far
    sub_bridges = []
    next_components = [c for c in combos[component] if component[port] in c and c in components_left]
    if not next_components:
        return ([component], sum(list(component)))
    for other_component in next_components:
        next_components_left = deepcopy(components_left)
        next_components_left.remove(other_component)
        next_port = 0
        if other_component[next_port] == component[port]:
            next_port = 1
        (sub_bridge, score) = search_combos(other_component, next_port, next_components_left)
        if score >= best_so_far[1]:
            best_so_far = (sub_bridge, score)
            print(sub_bridge, score)
        next_sub_bridge = deepcopy(sub_bridge)
        next_sub_bridge.append(component)
        sub_bridges.append((next_sub_bridge, score + sum(list(component))))
    best_sub_bridge = max(sub_bridges, key=lambda x: x[1])
    return best_sub_bridge

bridges = []
for component in components:
    next_components = deepcopy(components)
    next_components.remove(component)
    bridge1 = search_combos(component, 0, next_components)
    bridge2 = search_combos(component, 1, next_components)
    bridges.append(bridge1)
    bridges.append(bridge2)
    print("component",component,"searched. Max scores:",bridge1[1],bridge2[1])

print(max(bridges, key=lambda x: x[1]))