#убирает все согласные
CONSTANTS = u'бвгджзйклмнпрстфхцчшщъь'
result=[]
while True:
    word = raw_input (u'Введите слово ').decode('cp1251')
    if not word:
        break
    tmp=''
    for letter in word:
        if letter.lower() not in CONSTANTS:
            tmp+=letter
    result.append(tmp)

for write in result:
    print write
