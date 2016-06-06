import random
def generation():
    n = input(u'Введите число уровней лестницы: ')
    numbers = [0]
    while True:
        number = random.randint(-50, 50)
        if number == 0:
            continue
        if len(numbers) > n-2:
            break
        numbers.append(number)
    numbers.append(0)
    for i in numbers:
        print i
    return numbers
    

def foo(lst):
    lenght = len(lst)
    assert lenght >=  3
    if lenght == 3: return max((0, lst[1]))
    for i in xrange(lenght-2):
        m = max(lst[i], lst[i+1]) + lst[i+2]
        lst[i+2] = m
    return m
print(foo(generation()))
    
    
