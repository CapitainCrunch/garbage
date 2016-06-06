#гул€ет по директои€м, собирает, открывает txt файлы и делает частотный
#список всех слов в этих файлах
import codecs, os

def collect_files(way):
    files_names = []
    for root, dirs, files in os.walk(way):
        for x in files:
            files_names.append(root + u'\\' + x)
    return files_names

def collect_words():
    words = []
    for names in collect_files(u'.'):
        if names[-3:] == u'txt':
            f = codecs.open(names, 'r', 'utf-8-sig')
            for lines in f:
                lines = lines.strip().split()
                for words_line in lines:
                    words_line = words_line.strip(u'.,!?"\'ЂЕ()[]/ї*:;').lower()
                    words.append(words_line)
    return words          
            
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

frequency_list()
        
