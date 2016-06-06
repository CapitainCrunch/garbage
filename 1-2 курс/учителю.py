import re,codecs
f=codecs.open(u'bu.txt','r','utf-8-sig')
f2=codecs.open(u'new.txt','w','utf-8-sig')

for line in f:
    m=re.sub(u'\\bне\\b +',u'не_',line,flags=re.U)
    m=re.sub(u'\\bне(\\w*)',u'не_\\1',m,flags=re.U)
    m=re.sub(u'\\bНе\\b +',u'Не_',m,flags=re.U)
    m=re.sub(u'\\bНе(\\w*)',u'Не_\\1',m,flags=re.U)
    f2.write(m)
f2.close

