#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

target_presents = 36000000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def get_presents(number):
  # find prime factorisation
  current_prime = 0
  current_number = number
  exponents = {}
  while True:
    if current_prime >= len(primes):
      primes.append(current_number)
      exponents[current_number] = 1
      break
    if current_number % primes[current_prime] == 0:
      if primes[current_prime] not in exponents.keys():
        exponents[primes[current_prime]] = 0
      exponents[primes[current_prime]] += 1
      current_number /= primes[current_prime]
      current_prime = 0
      if current_number == 1:
        break
    else:
      current_prime += 1
  # sum of powers for each prime factor
  presents = 1
  for prime in exponents.keys():
    term = 0
    if exponents[prime] != 0:
      for j in range(exponents[prime]+1):
        term += prime ** j
      presents *= term
  presents *= 10
  return presents

presents = 0
house_number = 0
while True:
  house_number += 2
  presents = get_presents(house_number)
  if house_number % 1000 == 0:
    print str(house_number) + ": " + str(presents)
  if presents > target_presents:
    break
print house_number

# for i in range(2, 10):
#   presents = get_presents(i)
#   print str(i)+": "+str(presents)
#   if presents > target_presents:
#     print str(i)+": "+str(presents)
#     break