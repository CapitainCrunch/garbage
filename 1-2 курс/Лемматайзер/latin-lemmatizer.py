import codecs, re

def make_regex(nom, gen, gender):
    # делает регулярное выражение, распознающее все формы
    # данного существительного
    regex = u''
    if nom[-1:] == u'a' and gen[-2:] == u'ae':
        # 1 склонение
        regex = u'\\b' + nom[:-1] + u'(a[ems]?|arum|is)\\b'
    elif nom[-2:] == u'us' and gen[-1:] == u'i':
        # 2 склонение м. р.
        regex = u'\\b' + nom[:-2] + u'(u[ms]|is?|os?|orum)\\b'
    elif nom[-2:] == u'um' and gen[-1:] == u'i':
        # 2 склонение ср. р.
        regex = u'\\b' + nom[:-2] + u'(um|is?|o|a|orum)\\b'
    elif gen[-2:] == u'is' and gender == u'm' and\
         len(re.findall(u'[aeiouy]', gen)) > len(re.findall(u'[aeiouy]', nom)):
        # 3 неравносложное склонение м. р.
        regex = u'\\b' + nom + u'|' + gen[:-2] + u'(is|e[ms]?|um|ibus)\\b'
    return regex


def load_dict(fname):
    f = codecs.open(fname, 'r', 'utf-8')
    dictLemmas = {}  # ключи -- регулярные выражения, которые распознают
                     # все формы одного существительного; значения --
                     # леммы этих существительных
    for line in f:
        nom, gen, gender = line.strip().split(u';')
        regexWords = make_regex(nom, gen, gender)
        if regexWords == u'':
            continue  # если функция не распознала склонение
        dictLemmas[regexWords] = nom
    f.close()
    return dictLemmas


def process_text(fname, dictLemmas):
    # проставляет леммы в текстовом файле fname
    fIn = codecs.open(fname, 'r', 'utf-8')
    fOut = codecs.open('out.txt', 'w', 'utf-8')
    for line in fIn:
        for word in line.strip().split():
            lemma = u''
            for regex in dictLemmas:
                if re.search(regex, word.lower().strip(u'.,()?![]-')) != None:
                    lemma = dictLemmas[regex]
                    break   # лемма найдена, дальше можно не искать
            if len(lemma) > 0:   # если нашли какую-то лемму
                fOut.write(word + u'[' + lemma + u'] ')
            else:
                fOut.write(word + u' ')
        fOut.write(u'\r\n') # в конце каждого абзаца
    fIn.close()
    fOut.close()

if __name__ == u'__main__':
    dictLemmas = load_dict(u'latin_nouns.csv')
    process_text(u'Caesar.txt', dictLemmas)

    
