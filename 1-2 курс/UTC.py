#UTC показывает из html
import re, codecs

utc = []
utc_filtered = []
f = codecs.open(u'kiev.htm', 'r', 'utf-8-sig')
for line in f:
    line.lower()
    m = re.findall('UTC\W\d', line)
    if m != None:
        utc.append(m)
f.close()

for i in utc:
    for z in i:
        if z not in utc_filtered:
            utc_filtered.append(z)
    
for i in utc_filtered:
    for z in i:
        if z == '+' or z == '-':
            fOut = codecs.open(u'out.txt', 'w', 'utf-8')
            fOut.write(i + u'\r\n')
fOut.close()

