#программа спрашивает имя\номер и вносит в словарь.
#словарь записывает в csv - файл

import codecs

def fill():
    book = {}
    while True:
        name = raw_input(u'Input a name: ').decode('cp1251')
        number = raw_input(u'Input a number: ').decode('cp1251')
        if name == '':
            break
        book[name] = number
    return book 

for i in fill():
    print i

f = codecs.open(u'out.csv', 'w', 'utf-8')
for name in book:
    f.write(name + ';' + book[name] + u'\r\n')
    

f.close()

#вызвать функцию, перескакивает в начало, для красоты
if __name__ == u'__main__':
    fill()
