import codecs, re

def collect_lines(fname):
    words = []
    f = codecs.open(fname, 'r', 'utf-8')
    for line in f:
        line = line.lower()
        words.append(line)
    f.close()    
    return words

def swap():
    fOut = codecs.open (u'out.txt', 'w', 'utf-8-sig')
    for line in collect_lines(u'new.txt'):
            m = re.sub(u'\\b(\\w)(\\w)(\\w*?)(\\w)(\\w)\\b', u'\\1\\4\\3\\2\\5', line, flags = re.U)
            fOut.write(m)
    fOut.close()


if __name__ == u'__main__':
    swap()
