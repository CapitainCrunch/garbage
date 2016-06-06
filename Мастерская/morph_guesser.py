__author__ = 'Bogdan'
# encoding=utf-8

import codecs, re
from pprint import pprint

count = 0
f = codecs.open('morphodict2014.csv', 'r', 'utf-8')
for line in f:
    data = line.split(';')
    pprint(data)
    count += 1
    if count == 3: break
