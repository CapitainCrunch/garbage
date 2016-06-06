#прога спрашивает слова до пустого и печатает
#все слова в предложении до точки
arr = []
done = ''
word = raw_input('Word, please ').decode('cp1251')
while True:
    done = done + ' ' + word  
    if done[-1] == '.':
        arr.append(done)
        done = ''
    word = raw_input('Word, please ').decode('cp1251')
    if word == '':
        break
    

for i in arr:
    print i
