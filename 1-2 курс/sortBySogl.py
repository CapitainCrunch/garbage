a = []

while True:
    word = raw_input(u' Введите слово: ').decode('cp1251')
    a.append(word)
    if not word:
        break

def count_sogl(value):
    CONSTANTS = u'цкнгшщзхфвпрлдчсмтб'
    count = 0
    for a in CONSTANTS:
        b = a.lower()
        count += value.count(b)
    return count

a.sort(key=count_sogl)

for i in a:
    print i
