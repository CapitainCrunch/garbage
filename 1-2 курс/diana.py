import codecs, re
f = codecs.open('in.txt', 'r', 'utf-8')
fOut = codecs.open('out.txt', 'w', 'utf-8')
prs = [u'за', u'из', u'с', u'со', u'от', u'у', u'в', u'на', u'к', u'по',
       u'до', u'ко', u'За', u'Из', u'С', u'Со', u'От', u'У', u'В', u'На',
       u'К', u'По', u'До', u'Ко', u'О', u'о']
for line in f:
    for pr in prs:
        pred = re.findall(u'\\b' + pr + u'\\b' + u'\s\w+', line, flags = re.U)
        for i in pred:
                   fOut.write(i)
                   fOut.write('\r\n')
                   
                
