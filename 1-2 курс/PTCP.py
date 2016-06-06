#прога ищет слово после have
import re, codecs

words = []
f = codecs.open('new.txt', 'r', 'utf-8')
for line in f:
    for word in line.split():
        word = word.lower()
        word = word.strip(u'.,?!()/+=@#$%*-_`~')
        words.append(word)

f.close()

ptcp = []


for i in range(1, len(words)):
    if re.search(u'^ha(ve|s|d|ving)$', words[i]) != None:
        if words[i+2][-2:] == 'ed':
            ptcp.append(words[i+1])
    

for i in ptcp:
    print i 

