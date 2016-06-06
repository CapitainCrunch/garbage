#программа спрашиват у пользователя слова до тех пор, пока не введет 
#пустое место. За тем печатает все слова из массива, которые больше 5
arr = []
word = raw_input ('Type a word ')
arr.append (word)
while word != '':
    word = raw_input ('Type a word ')
    arr.append (word)

for i in arr:
    if len (i) > 5:
        print i
    
    
