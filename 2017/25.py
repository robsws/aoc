from collections import defaultdict
tape = defaultdict(int)
cursor = 0
state = 'a'

for i in range(12134527):
    if state == 'a':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'b'
        else:
            tape[cursor] = 0
            cursor -= 1
            state = 'c'
    elif state == 'b':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'a'
        else:
            tape[cursor] = 1
            cursor += 1
            state = 'c'
    elif state == 'c':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'a'
        else:
            tape[cursor] = 0
            cursor -= 1
            state = 'd'
    elif state == 'd':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 'e'
        else:
            tape[cursor] = 1
            cursor -= 1
            state = 'c'
    elif state == 'e':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'f'
        else:
            tape[cursor] = 1
            cursor += 1
            state = 'a'
    elif state == 'f':
        if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = 'a'
        else:
            tape[cursor] = 1
            cursor += 1
            state = 'e'

print(sum(tape.values()))