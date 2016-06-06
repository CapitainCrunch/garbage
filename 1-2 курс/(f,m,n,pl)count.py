import re, codecs


allcount = 0
fcount = 0
plcount = 0
mcount = 0

f = codecs.open(u'new.txt', 'r', 'utf-8-sig')
words = []
for line in f:
    for word in line.split():
        word = word.lower()
        word = word.strip(u'.,:;()[]<>/"\'?!')
        words.append(word)
f.close()

for i in words:
    allc = re.search(u'^всяк((ий)?|(ое)?|(ая)?|(ие)?|(ого)?|(ой)?|(их)?|(ому)?|(им)?|(ую)?|(ою)?|(ими)?|(и)?|(о)?|(а)?|(ом)?)?$', i)
    if allc != None:
        allcount += 1

    pl = re.search(u'^всяк((ие)?|(их)?|(ими)?|и?)$', i)
    if pl != None:
        plcount += 1

    f = re.search(u'^всяк((ая)?|(ой)?|(ую)?|(ою)?|а?)$', i)
    if f != None:
        fcount += 1

    m = re.search(u'^всяким$', i)
    if mcount != None:
        mcount += 1

lastcount = plcount + mcount
        
print (u' Всего встречается: ')
print allcount

print (u' В тексте больше: ')

if fcount > lastcount:
    print (u'Ж.р., ед.ч.')
elif fcount > plcount and fcount < lastcount:
    print (u' Неизвестно')
elif fcount < plcount:
    print (u'Мн.ч.')

