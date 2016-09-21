#!/usr/bin/env python

import re

a = 0
with open('funsites.txt','r') as file:
    for line in file:
        for result in re.finditer("(.*)(C|c)lean (C|c)lean(.*)", line):
            a += 1
print('Number of Clean sites with no issues in file: ' + str(a))


b = 0
with open('funsites.txt','r') as file:
    for line in file:
        for result in re.finditer("(.*)(B|b)lacklisted (C|c)lean(.*)", line):
            b += 1
print('Number of Blacklisted but Clean sites in file: ' + str(b))

c = 0
with open('funsites.txt','r') as file:
    for line in file:
        for result in re.finditer("(.*)(B|b)lacklisted (M|m)alwarefound(.*)", line):
            c += 1
print('Number of Blacklisted sites with Malwarefound sites in file: ' + str(c))

d = 0
with open('funsites.txt','r') as file:
    for line in file:
        for result in re.finditer("(.*)(C|c)lean (M|m)alwarefound(.*)", line):
            d += 1
print('Number of Clean sites with Malwarefound in file: ' + str(d))

