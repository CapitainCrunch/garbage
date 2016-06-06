__author__ = 'Bogdan'
#encoding=utf-8

class Object:
    pass

def create_person(name, surname, age, status):
    result = Object()
    result.name = name
    result.surname = surname
    result.age = age
    result.status = status
    return result

def create_fuzzy_animal(species, amount_of_fur):
    animal = Object()
    animal.species = species
    animal.amount_of_fur = amount_of_fur
    return animal

y = create_fuzzy_animal('Nyan-cat', 9000)
x = create_person('Valera', 'Nok', 3, 'privet')


data = vars(x)
data['birthday'] = 30.09


def f(*args):
    return args
#print f('lol')
#print f('hello', 'hi')

import time

def log(*args):
    print time.strftime('%H:%M:%S'), ' '.join(args)

def logstr(*args):
    print time.strftime('%H:%M:%S'), ' '.join([str(x) for x in args])
#logstr(10, 'hello')


def some(**kwargs):
    return kwargs
#print some(x=2, y=4)

a = {'a': 1, 'b': 2}
b = {'a': 4, 'x': 2}
a.update(b)
print a


def create(**values):
    result = Object()
    vars(result).update(values)
    return result
x = create(name ='Boris', surname='Orehov', age=33, status='cool guy')
print x.name

from lxml.html import parse
import codecs
text = codecs.open(fname, 'r', 'utf-8')
data = parse.text
data.getroot().child
data.getroot()
data.getroot().getchildren()
data.findall('body//href')
data.findall('body//a[img]')
