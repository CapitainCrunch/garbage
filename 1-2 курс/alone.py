import codecs, re


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


def paradigm(word):
    endings = [u'', u'm', u'rum', u's', u'e']
    endingEX = [u'is']
    forms = []
    for ending in endings:
        forms.append(word + ending)
    for ending in endingEX:
        forms.append(word[:-1] + ending)       
    return forms


def forms():
    all_forms = []
    words = collect_words(u'word.txt')
    for word in words:
        forms = paradigm(word)
        for form in forms:
            all_forms.append(form)
    return all_forms


def file_reader_add(fname):
    strings = []
    arr = forms()
    f = codecs.open(fname, 'r', 'utf-8-sig')
    for lines in f:
        lines = lines.split()
        for word in lines:
            word2 = word.strip(u'.,:;()[]<>/"\'?!')
            if word2 in arr:
                string = word + '[' + arr[0] +']' + ' '
                strings.append(string)
    f.close()


        
if __name__ == u'__main__':
    file_reader_add('new.txt')
