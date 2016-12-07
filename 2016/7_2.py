#!/usr/local/bin/python
import re

file = open("7_input.txt",'r')

aba_regex = re.compile(r'(?=((\w)(\w)\2))')

def get_abas(s):
  matches = re.findall(aba_regex, s)
  abas = []
  for match in matches:
    if match[1] != match[2]:
      abas.append(match[0])
  return abas

def get_abas_from_list(strings):
  abas = []
  for s in strings:
    abas.extend(get_abas(s))
  return abas

inside_brackets_regex = re.compile(r'\[(\w+)\]')
outside_brackets_regex = re.compile(r'(\w+)\[|\](\w+)')

total_ssl_ips = 0
for line in file:
  inside_brackets = re.findall(inside_brackets_regex, line)
  outside_brackets = re.findall(outside_brackets_regex, line)
  outside_brackets = map(lambda x: x[0] or x[1], outside_brackets)
  abas = get_abas_from_list(outside_brackets)
  babs = get_abas_from_list(inside_brackets)
  
  for aba in abas:
    expected_bab = aba[1]+aba[0]+aba[1]
    if expected_bab in babs:
      total_ssl_ips += 1
      break

print(total_ssl_ips)