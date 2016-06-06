#прога сортирует массив в алфавитном порядке не учитывая регистр
#i учитвает
a = [u'Продлить', u'Игру', u'невозможно', u'По', 'i', u'причине техничеcкой',
     u'ошибки', u'йогурт']

for i in range(len(a)):
    for j in range(1, len(a) - i):
        if a[j].lower().replace(u'i', u'й') < a[j - 1].lower().replace(u'i', u'й'):
            c = a[j - 1]
            a[j - 1] = a[j]
            a[j] = c
for i in a:
    print i
    
