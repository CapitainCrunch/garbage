__author__ = 'Bogdan'
# coding=utf-8

class Number(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        n = Number(self.x + other.x, self.y + other.y)
        return n

    def __repr__(self):
        return str(self.x) + ', ' + str(self.y)

number = Number(3, 5)
n2 = Number(1, 2)
n3 = number + n2
print n3