import codecs, random

riddle = {}
f = codecs.open(u'dictionary.csv', 'r', 'utf-8')
for line in f:
    line = line.strip()
    promt, solve = line.split(';')
    riddle[promt] = solve


def make_choice():

     
        
        
    written_answers = []
    key = random.choice(riddle.keys())
    
    if key == u'Потушить':
        print (key + ' ' + '.'*5)
        answer = raw_input(u'Попробуй отгадать загаданное слово: ').decode('cp1251')
        if answer == u'пожар':
            print (u' Ты угадал слово, молодец!')
        else:
            written_answers.append(answer)
            
            while len(written_answers) != 6:
                answer = raw_input(u'Не-а. Неправильно. Попробуй еще раз: ').decode('cp1251')
                written_answers.append(answer)
                
                if answer == u'пожар':
                    print (u' Ты угадал слово, молодец!')
                    break
                if len(written_answers) == 6:
                    print (u' Ты проиграл')

    if key == u'Наводить':
        print (key + ' ' + '.'*7)
        answer = raw_input(u'Попробуй отгадать загаданное слово: ').decode('cp1251')
        if answer == u'порядок':
            print (u' Ты угадал слово, молодец!')
        else:
            written_answers.append(answer)
            while len(written_answers) != 7:
                answer = raw_input(u'Не-а. Неправильно. Попробуй еще раз: ').decode('cp1251')
                written_answers.append(answer)
                if answer == u'порядок':
                    print (u' Ты угадал слово, молодец!')
                    break
                if len(written_answers) == 7:
                    print (u' Ты проиграл')            

    if key == u'Включить':
        print (key + ' ' + '.'*4)
        answer = raw_input(u'Попробуй отгадать загаданное слово: ').decode('cp1251')
        if answer == u'свет':
            print (u' Ты угадал слово, молодец!')
        else:
            written_answers.append(answer)
            while len(written_answers) != 4:
                answer = raw_input(u'Не-а. Неправильно. Попробуй еще раз: ').decode('cp1251')
                written_answers.append(answer)
                if answer == u'свет':
                    print (u' Ты угадал слово, молодец!')
                    break
                if len(written_answers) == 4:
                    print (u' Ты проиграл')            


    if key == u'Тратить':
        print (key + ' ' + '.'*6)
        answer = raw_input(u'Попробуй отгадать загаданное слово: ').decode('cp1251')
        if answer == u'деньги':
            print (u' Ты угадал слово, молодец!')
        else:
            written_answers.append(answer)
            while len(written_answers) != 6:
                answer = raw_input(u'Не-а. Неправильно. Попробуй еще раз: ').decode('cp1251')
                written_answers.append(answer)
                if answer == u'деньги':
                    print (u' Ты угадал слово, молодец!')
                    break
                if len(written_answers) == 6:
                    print (u' Ты проиграл') 


    if key == u'Сочинять':
        print (key + ' ' + '.'*5)
        answer = raw_input(u'Попробуй отгадать загаданное слово: ').decode('cp1251')
        if answer == u'песни':
            print (u' Ты угадал слово, молодец!')
        else:
            written_answers.append(answer)
            while len(written_answers) != 5:
                answer = raw_input(u'Не-а. Неправильно. Попробуй еще раз: ').decode('cp1251')
                written_answers.append(answer)
                if answer == u'песни':
                    print (u' Ты угадал слово, молодец!')
                    break
                if len(written_answers) == 5:
                    print (u' Ты проиграл')
print (
    u"""
Привет! Я хочу сыграть с тобой в игру Угадайка-Дополняйка.
Я загадала существительное и ты должен будешь его угадать. Чтобы тебе помочь, вот тебе подсказки:
1)Многоточие содержит столько точек, сколько букв в слове
2)Сколько букв в слове, столько  и попыток у тебя его отгадать
Удачи!
""")

if __name__ == u'__main__':
    make_choice()

