__author__ = 'Bogdan'
#encodings=utf-8



class Rectangle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def length(self):
        return self.x

    @length.setter
    def length(self, value):
        if value > 0:
            self.x = value

    @property
    def width(self):
        return self.x

    @width.setter
    def width(self, value):
        if value > 0:
            self.x = value

r = Rectangle(5,10)
print r.x
a = r.x - 50
print a
r.length = -10
print r.length


class FreqList(object):

    def load_text(self, fname):
        pass

    @property
    def freq_list(self):
        pass