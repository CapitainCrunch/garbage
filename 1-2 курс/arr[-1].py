# Программа должна спрашивать у пользователя слова до тех пор, пока он не
#введёт пустое слово. После этого программа должна вывести на экран
#каждое из введённых слов задом наперёд (каждое слово на отдельной строчке).
arr = []
word = raw_input ('Type a word ')
arr.append (word)
while word != '':
    word = raw_input ('Type a word ')
    arr.append (word)

for i in arr:
    print i [::-1]
