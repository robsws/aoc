import sys
import solutions
# import visualisations

(day, part) = sys.argv[1:3]
filename = "inputs/"+day+".txt";
file = open(filename,'r')
lines = file.read().splitlines()
solver = solutions.get_solver(day, part)
solution = solver(lines)
print("day",day,"part",part,":",str(solution))