import sys

print('generating queue 1')
gen1 = int(sys.argv[1])
valid_gen_queue1 = []
while(len(valid_gen_queue1) < 5000000):
    gen1 = (gen1 * 16807) % 2147483647
    if gen1 % 4 == 0:
        valid_gen_queue1.append(gen1)

print('generating queue 2')
gen2 = int(sys.argv[2])
valid_gen_queue2 = []
while(len(valid_gen_queue2) < 5000000):
    gen2 = (gen2 * 48271) % 2147483647
    if gen2 % 8 == 0:
        valid_gen_queue2.append(gen2)

print('comparing queues')
matching = 0
for pair in zip(valid_gen_queue1, valid_gen_queue2):
    if int(pair[0] & 65535) == int(pair[1] & 65535):
        matching += 1

print('part2: '+str(matching))