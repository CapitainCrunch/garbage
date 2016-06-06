__author__ = 'Bogdan'
# encoding=utf-8
from pprint import pprint
from pymystem3 import Mystem
import codecs, re

mystem = Mystem()



fulltext = ''
textout = ''
f = codecs.open('1.txt', 'r', 'utf-8')
for line in f: fulltext+=line
lemmas = mystem.analyze(fulltext)
for lemm in lemmas:
    for k,v in lemm.items():
        if k == 'analysis':
            for new in v:
                for n1,n2 in new.items():
                    #print n1,n2
                    textout += n1+' '+n2
                    textout += '\r\n'
print textout

fout = codecs.open('out.txt', 'w', 'utf-8')

m = re.findall('lex\s(\w+)', textout, flags=re.U)
a = m[:999]
print len(set(a))
