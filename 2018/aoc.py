import sys
import solutions
# import visualisations

if len(sys.argv) == 3:
    (day, part) = sys.argv[1:3]
    filename = "inputs/"+day+".txt"
elif len(sys.argv) == 4:
    (day, part, filename) = sys.argv[1:4]
else:
    print("Usage: python aoc.py <day> <part> [<custom filename>]")
    exit(1)
file = open(filename,'r')
lines = file.read().splitlines()
solver = solutions.get_solver(day, part)
solution = solver(lines)
print("day",day,"part",part,":",str(solution))