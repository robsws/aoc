import sys

gen1 = int(sys.argv[1])
gen2 = int(sys.argv[2])
matching = 0

for i in range(40000000):
    gen1 = (gen1 * 16807) % 2147483647
    gen2 = (gen2 * 48271) % 2147483647
    if int(gen1 & 65535) == int(gen2 & 65535):
        matching += 1

print('part1: '+str(matching))