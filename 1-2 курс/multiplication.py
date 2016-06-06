# Программа печатает таблицу умножения размером n x n

n = input('Input the number of rows: ')

row = 1  # row -- это счётчик строк
while row <= n:
    column = 1  # column -- это счётчик чисел внутри одной строки
    while column <= n:
        print row * column,
        column += 1
    print "\n", # по окончании каждой строчки начинаем новую строчку
    row += 1    # не забываем на каждом шаге увеличивать row на 1
