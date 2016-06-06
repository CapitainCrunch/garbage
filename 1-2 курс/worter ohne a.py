# -*- coding: cp1251 -*-
import re, codecs

f = codecs.open(u'new.txt', 'r', 'utf-8-sig')
words = []
wordnota = []
for line in f:
    for word in line.split():
        word = word.lower()
        word = word.strip(u'.,:;()[]<>/"\'?!')
        words.append(word)
f.close()

for i in words:
    if u'а' not in i:
        wordnota.append(i)

for i in wordnota:
    print i
