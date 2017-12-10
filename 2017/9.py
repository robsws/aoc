import sys

input_filename = sys.argv[1]
file = open(input_filename,'r')

stream = file.read()
index = 0
group_level = 0
score = 0
garbage = False
amount_of_garbage = 0
while index < len(stream) and stream[index] != "\n":
    char = stream[index]
    if char == '{' and not garbage:
        group_level += 1
    elif char == '}' and not garbage:
        score += group_level
        group_level -= 1
    elif char == '<' and not garbage:
        garbage = True
    elif char == '>':
        garbage = False
    elif char == '!':
        index += 1
    elif garbage:
        amount_of_garbage += 1
    index += 1

print('part 1: '+str(score))
print('part 2: '+str(amount_of_garbage))
