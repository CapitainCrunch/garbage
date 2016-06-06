import codecs
fOut = codecs.open(u' Out.html', 'w', u'utf-8-sig')
arr = []
while True:
    word = raw_input(u'Напиши слово: ').decode('cp1251')
    arr.append(word)
    if word == '':
        break

frst_part = u'''
<html>
<title>My page</title>
<body>
<h1>Список</h1>
<ul>
'''

lst_part = u'''
</ul>
</body>
</html>
'''

fOut.write(frst_part)
for word in arr:
    if u'А' in word or u'а' in word:
        fOut.write('<li>' + word + '</li>')
fOut.write(lst_part)
fOut.close()
