#создаем класс Стола
class Table:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.length = 130
        self.width = 45
        self.color = u'brown'

    def move(self, x, y):
        self.x += x
        self.y -= y

#создаем стол

table1 = Table()
print table1.color
print table.width += 10
print table1.move(50, 50)
