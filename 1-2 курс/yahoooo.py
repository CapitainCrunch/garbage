#В этом домашнем задании программа должна открывать файл с русским текстом в кодировке UTF-8 и распечатывать из него по одному разу все встретившиеся в нём:
#формы глагола "найти"

import re, codecs

words = []
k = []
complete = []


f = codecs.open(u'найти.txt', 'r', 'utf-8-sig')
for line in f:
       for word in line.split():
           word = word.lower()
           word = word.strip(u'.,?!')
           words.append(word)
f.close()

for i in words:
       m = re.search(u'^на(й|ш)(д|е|л)(у|е|л|а|о|и|д|я)(ш|т|м|н|с)(и|ь|я|о|а|е|с|н|ы)(й|е|ь)$', i)
       k.append(i)       
       while m != None:
              for i in words:
                     m = re.search(u'^на(й|ш)(д|е|л)(у|е|л|а|о|и|д|я)(ш|т|м|н|с)(и|ь|я|о|а|е|с|н|ы)(й|е|ь)$', i)
                     k.append(i)


for i in k:
       if i not in complete:
              complete.append(i)

for i in complete:
       print i
