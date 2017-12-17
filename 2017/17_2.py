import sys

step = int(sys.argv[1])
current_position = 0
buffer_len = 1
value_after_zero = -1
for i in range(1, 50000000):
    current_position = ((current_position + step) % (i)) + 1
    if(current_position == 1):
        value_after_zero = i

print('part 2: '+str(value_after_zero))