#encoding=utf-8
def mergeSort(arr):

    if len(arr) <= 1:
        return arr
 
    i = len(arr) / 2
    left = mergeSort(arr[:i])
    right = mergeSort(arr[i:])
 
    final = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:   
            final.append(right.pop(0))
        else:
            final.append(left.pop(0))
 
    if len(left) > 0:
        final.extend(mergeSort(left))
    else:
        final.extend(mergeSort(right))
 
    return final

#у нас n итераций, потому что входных данных n, а потом бинарные действия (делим на два)

#3 задание
#это пример кода лесенки и нахождения максимальной суммы, примерная стратегия
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



#это только идея:  использовать bucket sort, а потом динамическое решение: брать первые два элемента массива и прибавлять
#к ним третий и смотреть, получилась ли данное число, если нет, то берем 4ое и т.д. и так далее по всему массиву