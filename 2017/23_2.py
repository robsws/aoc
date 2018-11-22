h = 0
for b in range(107900, 124901, 17):
    for e in range(2, b):
        if b % e == 0:
            h += 1
            break
print(h)