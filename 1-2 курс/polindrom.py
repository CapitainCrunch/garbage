#спрашивает слова до пробела и печатает слова до
#полиндрома(шалаш, мадам)
arr = []

while True:
    word = raw_input('Word, please ').decode('cp1251')
    arr.append(word)
    if word == '':
        break

for i in arr:
    if i != i[::-1]:
        print i
    else:
        break
