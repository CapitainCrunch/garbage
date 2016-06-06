#программа спрашивает у пользователя что-то
#и выводит что-то без согласных
word = raw_input (u'Введите слово ').decode('cp1251')
new_word = ''
CONSTANTS = u'цкнгшщзхфвпрлдчсмтб'

for letter in word:
    if letter.lower() not in CONSTANTS:
        new_word += letter
   
print new_word


