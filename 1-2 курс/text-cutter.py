import re, codecs, os

f = codecs.open(u'text.txt', 'r', 'utf-8')
fChapter = None

for line in f:
    m = re.search(u'^\\s*([IVXLDCM]+)\\.\\s*$', line.strip())
    if m != None:
        chapterName = m.group(1)
        print u'Chapter ' + chapterName
        os.makedirs(chapterName)
        if fChapter != None:
            fChapter.close()  # закрыть файл с предыдущей главой,
                              # если текущая глава не является первой
        fChapter = codecs.open(chapterName + u'/chapter' +\
                               chapterName + u'.txt', 'w', 'utf-8')
    if fChapter != None:
        # если это уже текст какой-то главы
        fChapter.write(line)
f.close()
if fChapter != None:
    fChapter.close()
