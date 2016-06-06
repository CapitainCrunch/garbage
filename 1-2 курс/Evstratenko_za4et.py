import codecs, re, os
f = codecs.open('new.txt', 'r', 'utf-8')
f1 = codecs.open('out.txt', 'w', 'utf-8')
verb = [u'Думаю', u'Думал', u'Думала', u'Думаешь', u'Думай', u'Думайте',
        u'Думаем', u'Думало', u'Думаем', u'Думали', u'Думаете', u'Думают',
        u'Думает', u'думаю', u'думал', u'думала', u'думаешь', u'думай',
         u'думайте', u'думаем', u'думало', u'думаем', u'думали',
         u'думаете', u'думают', u'думает']
fnd = []    
for line in f:
    for i in verb:
        found = re.findall(u'\\b' + i + u'\\b' + u'.' + u'\s\w+', line, flags = re.U)
        for k in found:
            m = re.search(u'(\w+).\s\w+', k, flags = re.U)
            if m != None:
                m = m.group(1)
                if m not in fnd:
                    fnd.append(m)
            f1.write(k)
            f1.write('\r\n')
            s = re.search(u'(.*?(' + k + u').*)', line, flags = re.U)
            if s != None:
                s = s.group(1)
            try:
                os.makedirs('C:\\Users\\student\\Desktop\\1\\' + str(len(fnd)))
                f39 = codecs.open('C:\\Users\\student\\Desktop\\1\\' + str(len(fnd)) + u'\\' + u'азазаз' + u'.txt', 'w', 'utf-8')
            except OSError:
                    pass               
f1.close()

