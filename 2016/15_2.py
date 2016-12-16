#!/usr/local/bin/python
t = 0
while not((10+t+1)%13 == 0 and (15+t+2)%17 == 0 and (17+t+3)%19 == 0 and (1+t+4)%7 == 0 and (t+5)%5 == 0 and (1+t+6)%3 == 0 and (t+7)%11 == 0):
  t += 1
print(t)
