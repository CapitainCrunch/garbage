__author__ = 'Bogdan'
# coding=utf-8

class Student(object):
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.department = ''
        self.year = ''

    def next_year(self):
        years = [u'1 бак', u'2 бак', u'3 бак', u'4 бак', u'1 маг', u'2 маг']
        for i in xrange(5):
            if self.year == years[i]:
                self.year = years[i+1]
                return True
            else:
                print 'Выпускник'
                return False

    def old(self):
        years = [u'1 бак', u'2 бак', u'3 бак', u'4 бак', u'1 маг', u'2 маг']
        for k, v in enumerate(years):
            if self.year == v:
                return k


    def __lt__(self, other):
        if self.old() < other.old():
            return True
        return False


class University(object):
    def __init__(self):
        self.st = Student()

    def add_student(self, name, surname):
        students = []
        s = Student()
        s.name = name
        s.surname = surname
        s.department = 'Зачислить студента на первый курс бакалавриата'
        s.year = u'1 бак'
        students.append(s)
        return students

    def end_year(self):
        for i, k in enumerate(add_student):
            k.next_year()
            if False:
                add_student.pop(i)



#запутался совсем как связать класс University и Student :(


