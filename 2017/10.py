import sys

input_filename = sys.argv[1]
file = open(input_filename,'r')
lengths = map(int, file.read().rstrip().split(','))
knot = list(range(256))
index = 0
skip = 0

for length in lengths:
    # reverse the order of the elements in sublist
    if index + length > len(knot):
        reversed_section = list(reversed(knot[index:index+length] + knot[0:(index+length)-len(knot)]))
        knot[index:index+length] = reversed_section[0:len(knot) - index]
        knot[0:(index + length) - len(knot)] = reversed_section[len(knot) - index:]
    else:
        knot[index:index+length] = list(reversed(knot[index:index+length]))
    # move current position by length + skip
    index += length + skip
    if index > len(knot):
        index = index % len(knot)
    # increment skip by one
    skip += 1
    print(knot)
print('part 1: '+str(knot[0] * knot[1]))