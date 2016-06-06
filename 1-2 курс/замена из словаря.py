#замена в тексте из словаря. слева - заменяемое
import codecs, re


def load_dict(fname):
    f = codecs.open(fname, 'r', 'utf-8-sig')
    dictSwap = {} 
    for line in f:
        old, new = line.strip().split(u';')
        if len(old) > 4:
            dictSwap[old] = new
    f.close()
    return dictSwap


def process_text(fname, dictionary):
    fIn = codecs.open(fname, 'r', 'utf-8')
    fOut = codecs.open('out.txt', 'w', 'utf-8')
    for line in fIn:
        for word in line.strip(u'.,()?![]-').split():
            swapped = word
            for swap in dictionary:
                swapped = re.sub(old, dictionary[old] + u'\\1', swapped, flags = re.U)
            if swapped != word:
                fOut.write(swapped + ' ')
            else:
                fOut.write(word + ' ')
        fOut.write(u'\r\n')
                    
    
    fIn.close()
    fOut.close()
if __name__ == u'__main__':
    dictionary = load_dict(u'new_dict.csv')
    process_text(u'new.txt', dictionary)

    
