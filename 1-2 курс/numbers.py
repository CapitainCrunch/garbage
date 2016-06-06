#программа спрашивает у вользователя чила пока тот не введет 0
#потом выводит числа, сумма которых меньше ста
arr = []

while True:
    number = input('Input a number: ')
    arr.append(number)
    if number == 0:
        break
s = 0
for i in arr:
    s += i
    if s < 100:
        print i
    else:
        break
    
    
            
