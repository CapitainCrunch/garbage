import os, codecs

def collect_words(fname):
    words = []
    f = codecs.open(fname, 'r', 'utf-8')
    for line in f:
        for word in line.split():
            word = word.lower()
            word = word.strip(u'.,?!')
            words.append(word)
    return words

words = []
for root, dirs, files in os.walk(u'./'):
    for fname in files:
        fname = os.path.join(root, fname)
        if fname[-4:] != u'.txt':
            continue
        words += collect_words(fname)

fOut = codecs.open(u'words.txt', 'w', 'utf-8')
for word in words:
    fOut.write(word + u'\r\n')
fOut.close()


    
