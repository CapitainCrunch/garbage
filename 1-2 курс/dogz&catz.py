#заменяет в тхт кошки на собак
import codecs, re
f = codecs.open(u'new.txt', 'r', 'utf-8-sig')
fOut = codecs.open(u'swapped.txt', 'w', 'utf-8')
for line in f:
    m = re.sub(u'коше?к', u'собак', line)
    m = re.sub(u'Коше?к', u'Собак', m)
    m = re.sub(u'кот\\b', u'пёс', m, flags = re.U)
    m = re.sub(u'Кот\\b', u'Пёс', m, flags = re.U)
    m = re.sub(u'кошач', u'собач', m)
    m = re.sub(u'Кошач', u'Собач', m)
    fOut.write(m)

fOut.close()
