#во сколько раз длинне самая длинная строка самой короткой
import codecs



f = codecs.open(u'new.txt', 'r', 'utf-8')
words = []
for line in f:
    words += line.split()

for i in words:
    a = len(max(words, key=len))
f.close()

f = codecs.open(u'new.txt', 'r', 'utf-8')

for x in words:
    b = len(min(words, key=len))
f.close()

f = codecs.open(u'new.txt', 'r', 'utf-8')
print a/b



f.close()
