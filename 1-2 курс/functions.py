def collect_words(filename):
    f = codecs.open(filename, 'r', 'utf-8')
    words = []
    for line in f:
        line = line.lower()
        for word in line.split():
            word = word.strip(u'.,:;()[]<>/"\'?!')
            words.append(word)
    f.close()
    return words

def first_letter():
    first_letter_swapped = []
    for line in collect_lines(u'new.txt'):
        re.sub = (u'(.?)(.?)(.*?)\\b', '\\2\\1\\3', line, flags = re.U)
        first_letter_swapped.append(line)
        f.close()
    return first_letter_swapped
    
def first_last():
    first_last = []
    for line in collect_lines(u'new.txt'):
        re.sub = (u'(.?)(.*?)(.?)\\b', '\\3\\2\\1', line, flags = re.U)
        first_last.append(line)
        f.close()
    return first_last


def frequency_list():
    csv = codecs.open(u'frequency.csv', 'w', 'utf-8-sig')
    frequency = {}
    for word in collect_words():
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1
    for i in frequency:
        csv.write(i + u';' + str(frequency[i]) + u'\r\n')
    csv.close()



















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

