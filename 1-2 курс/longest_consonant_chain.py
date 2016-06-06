import codecs, re

def consonant_chain_length(word):
    # функция находит длину самой длинной цепочки согласных
    # в слове word
    chains = re.findall(u'[бвгджзклмнпрстфхцчшщ]+', word)
    maxlen = 0
    for chain in chains:
        if len(chain) > maxlen:
            maxlen = len(chain)
    return maxlen


def words_with_longest_chain(words):
    # функция находит слова из массива words с самыми длинными
    # цепочками согласных
    maxlen = 0
    words_found = []
    for word in words:
        word = word.strip(u'.,!?"\'()[]/*:;').lower()
        chainlen = consonant_chain_length(word)
        if chainlen > maxlen:
            # если до сих пор мы не встречали слов с такой
            # длинной цепочкой согласных, нужно стереть все
            # слова, которые мы до сих пор хранили в words_found
            maxlen = chainlen
            words_found = []
        if chainlen >= maxlen:
            words_found.append(word)
    return words_found


def main(filename):
    words = []
    f = codecs.open(filename, 'r', 'utf-8')
    for line in f:
        words += line.split()
    f.close()
    
    words_to_print = words_with_longest_chain(words)
    for word in sorted(words_to_print):
        print word


if __name__ == u'__main__':
    main(u'text.txt')
