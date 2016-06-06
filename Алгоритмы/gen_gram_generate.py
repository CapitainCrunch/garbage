__author__ = 'Bogdan'
# encoding=utf-8
from random import random
terminal_symbols = [u'NP', u'A', u'N']
transitions = {u'NP': [(0.5, u'A', u'N'), (1, u'N', u'A')], u'N': [(0.2, u'cat'), (1, u'dog')],
         u'A': [(0.2, u'big'), (0.4, u'small'), (0.6, u'huge'), (1, u'little')]}

sentence = []
def gen_sentence(transitions, terminal_symbols, first_symbol):
    for key, value in transitions.items():
        if key == first_symbol:
            for v in value:
                print v[-1]
                if random() < v[0] and v[-1] in terminal_symbols:
                    for i in xrange(1, len(v)):
                        gen_sentence(transitions, terminal_symbols, first_symbol = v[i])
                    break
                if v[-1] not in terminal_symbols and random() < v[0]:
                    sentence.append(v[-1])
                    break
            break
    return ' '.join([word for word in sentence])


print gen_sentence(transitions, terminal_symbols, 'NP')
