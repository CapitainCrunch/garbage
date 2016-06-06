import codecs

def paradigm(word):
    endings = [u'o', u's', u't', 'mus', 'tis', 'unt']
    forms = []
    stem = word[:-1]
    for ending in endings:
        forms.append(stem + ending)
    return forms


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


def print_csv(frequencies):
    f = codecs.open(u'table.csv', 'w', 'utf-8')
    for key in frequencies:
        f.write(key + u';' + str(frequencies[key]) + u'\r\n')
    f.close()

        
def main():
    # с этого места начинается работа программы
    word = raw_input(u'Введите глагол 4 спряжения: ').decode('cp1251')
    forms = paradigm(word)
    for form in forms:
        print form
    print u'Part 1 done.\n'

    # Соберём слова из текста в массив words
    words = collect_words(u'text.txt')

    # Распечатаем все слова, стоящие перед одной из форм
    # глагола, и заодно подсчитаем, сколько раз они встречаются в тексте
    frequencies = {}
    for i in range(1, len(words)):
        # Начинаем с 1, потому что нам может понадобиться
        # записать слово с номером i - 1. Если начать с нуля,
        # это может приведёт к ошибке (если первое слово текста
        # окажется формой введённого глагола).
        if words[i] in forms:
            print words[i - 1]
            if words[i - 1] in frequencies:
                frequencies[words[i - 1]] += 1
            else:
                frequencies[words[i - 1]] = 1
    print u'Part 2 done.\n'

    # Теперь запишем всё это в csv:
    print_csv(frequencies)
    print u'Part 3 done.\n'


if __name__ == u'__main__':
    main()

        
