__author__ = 'Bogdan'
# encoding=utf-8
import time
import codecs

class Hash:
    def __init__(self, string, size):
        self.str = string
        self.hash = 0

        for i in xrange(0, size):
            self.hash += ord(self.str[i])

        self.init = 0
        self.end = size

    def update(self):
        if self.end <= len(self.str)-1:
            self.hash -= ord(self.str[self.init])
            self.hash += ord(self.str[self.end])
            self.init += 1
            self.end += 1

    def digest(self):
        return self.hash

    def text(self):
        return self.str[self.init:self.end]


def rabin_karp(substring, string):
    if substring == None or string == None: return False
    if substring == '' or string == '': return False
    if len(substring) > len(string): return False
    hs = Hash(string, len(substring))
    hsub = Hash(substring, len(substring))
    hsub.update()

    for i in xrange(len(string) - len(substring)-1):
        if hs.digest() == hsub.digest():
            if hs.text() == substring:
                return True
        hs.update()
    return False


test_strings = [('sun', 'sunshine'), ('sun', 'Say hello to the sunshine in the middle of the universe'),
                ('sunshine', 'Say hello to the sunshine in the middle of the universe'), ('sun', 'sun'),
                ('sunn', 'Say hello to the sunshine in the middle of the universe'), ('sun', 'sunn'),
                ('sunn', 'Say hello to the sunshine in the middle of the universe')]
print len(test_strings)


#по такому же принципу выводил таблицу написанной функции
f2 = codecs.open('table2.csv', 'w', 'utf8')
for _ in xrange(10):
    for sub, string in test_strings:
        st = time.clock()
        if sub in string:
            fin = time.clock()
            f2.write(str(st) + ';' + str(fin) + ';')
        else:
            fin2 = time.clock()
            f2.write(str(st) + ';' + str(fin2) + ';')
    f2.write('\r\n')