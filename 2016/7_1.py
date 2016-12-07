#!/usr/local/bin/python
import re

file = open("7_input.txt",'r')

abba_regex = re.compile(r'(\w)(\w)\2\1')

def has_abba(s):
  matches = re.findall(abba_regex, s)
  for match in matches:
    if match[0] != match[1]:
      return True
  return False

def check_list_for_abba(strings):
  for s in strings:
    if has_abba(s):
      return True
  return False

inside_brackets_regex = re.compile(r'\[(\w+)\]')
outside_brackets_regex = re.compile(r'(\w+)\[|\](\w+)')

total_tls_ips = 0
for line in file:
  inside_brackets = re.findall(inside_brackets_regex, line)
  outside_brackets = re.findall(outside_brackets_regex, line)
  outside_brackets = map(lambda x: x[0] or x[1], outside_brackets)
  # Check that ABBA does not exist inside brackets
  if check_list_for_abba(inside_brackets):
    continue
  # Check that ABBA does exist outside brackets
  if check_list_for_abba(outside_brackets):
    total_tls_ips += 1

print(total_tls_ips)