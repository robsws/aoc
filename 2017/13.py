import sys

input_filename = sys.argv[1]
file = open(input_filename,'r')
lines = file.read().splitlines()
scanners = [tuple(map(int, l.split(': '))) for l in lines] 

def severity(scanners):
    return sum([t * r for (t, r) in scanners if t % (2*(r-1)) == 0])

def times_caught(scanners, offset):
    return sum([1 for (t, r) in scanners if (t+offset) % (2*(r-1)) == 0])

offset = 0
while times_caught(scanners, offset) > 0:
    offset += 1

print('part 1: '+str(severity(scanners)))
print('part 2: '+str(offset))