import sys

step = int(sys.argv[1])
buffer = [0]
current_position = 0
for i in range(1, 2018):
    current_position = (current_position + step) % (i)
    buffer.insert(current_position+1, i)
    current_position += 1

answer_index = (buffer.index(2017)+1) % len(buffer)
print('part 1: '+str(buffer[answer_index]))