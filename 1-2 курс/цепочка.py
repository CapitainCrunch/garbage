#слово из текста с самой длинной цепочкой согласных
import codecs, re
f = codecs.open( u'book1.txt', 'r', 'utf-8-sig')
words = []
for line in f:
    line = re.sub(u'\[!\";:?\(\)\.\,\\\]', u'', line, flags = re.U)
    line = line.lower()
    words += line.split()
f.close()

current_max = 0
arrWords = []
arrWordsFiltered = []
for i in words:
    sogl = re.findall(u'[йцкнгшщзхфвпрлджчмтб]+', i, flags = re.U)
    lenMax = 1
    for s in sogl:
        if len(s) > lenMax:
            lenMax = len(s)
    if lenMax == current_max:
        current_max = lenMax
        arrWords.append(i)
    if lenMax > current_max:
        arrWords = []
        current_max = lenMax
        arrWords.append(i)
        

for i in arrWords:
    i = i.strip(u',!";.»;"?')
    if i not in arrWordsFiltered:
        arrWordsFiltered.append(i)

for i in arrWordsFiltered:
    print i
