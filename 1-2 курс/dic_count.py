import codecs, re

f = codecs.open( u'war.txt', 'r', 'utf-8-sig')
words = []
for line in f:
    line = line.lower()
    words += line.split()
f.close()


word_two_chain = []
for i in words:
    chains = re.findall(u'[ауоыиэяюёе]+', i, flags = re.U)
    lenMax = 2
    for chain in chains:
        if len(chain) >= lenMax:
            word_two_chain.append(i)

vowels_chain = []
for i in word_two_chain:
    chains = re.findall(u'[ауоыиэяюёе]+', i, flags = re.U)
    maxlen = 2
    for chain in chains:
        if len(chain) >= maxlen:
            vowels_chain.append(chain)



dic_count = {}

for key in vowels_chain:
    key = key.lower()
    if key in dic_count:
        dic_count[key] += 1
    else:
        dic_count[key] = 1

fOut = codecs.open(u'out.csv', 'w', 'utf-8')
for key in dic_count:
    fOut.write(key + u';' + str(dic_count[key]) + u'\r\n')
fOut.close()


