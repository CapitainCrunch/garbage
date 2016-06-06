import codecs, re

fIn = codecs.open (u'new.txt', 'r', 'utf-8-sig')
fOut = codecs.open (u'out.txt', 'w', 'utf-8-sig')
keys = codecs.open (u'keys.txt', 'w', 'utf-8-sig')
for line in fIn:
    for word in line.strip().split():
        if u'a' in word or u'o' in word or u'u' in word or u'ä' in word or u'ö' in word or u'ü' in word:
            keys.write(word + '\r\n')
            word = re.sub (u'a|ä', u'A', word, flags = re.U)
            word = re.sub (u'o|ö', u'O', word, flags = re.U)
            word = re.sub (u'u|ü', u'U', word, flags = re.U)
            fOut.write (word + u' ')
        else:
            fOut.write (word + u' ')

fIn.close()
fOut.close()
keys.close()
            

