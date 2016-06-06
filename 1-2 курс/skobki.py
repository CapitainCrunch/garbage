# -*- coding: cp1251 -*-
import re, codecs

f = codecs.open(u'new.txt', 'r', 'utf-8-sig')
words = []

for line in f:
    line.lower()
    m = re.findall('\\(.*?\\)', line)
    
    if m != None:
        words.append(m)
        
for i in words:
       for z in i:
           print z[1:-1]
       
f.close()


