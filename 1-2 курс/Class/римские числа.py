__author__ = 'Bogdan'
# coding=utf-8

class Number(object):
    def __init__(self, string):
        self.string = string
        self.value = None
        self.count = None
        d = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}
        for k, v in d.iteritems():
            if self.string == k:
                self.value = v

    def translate(self):
        d = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}
        for k, v in d.iteritems():
            if self.string == k:
                self.value = v
        return self.value

    def __add__(self, other):
        n = Number(self.string.translate() + other.string.translate())
        self.count = n.count
        return self.count


    def __repr__(self):
        return str(self.value)

number = Number('CV')
print (number.value)
