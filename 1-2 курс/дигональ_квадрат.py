row = input('¬едите число: ')
column = 0
a = 0
if row == 0:
    print 'картинка не может быть напечатана.'
if row == 1:
    print 'x'
if row > 1:
    print 'x' * row
    while column != row - 2:
        b = row - 3 - a
        print 'x' + (' ' * a) + 'x' + (' ' * b) + 'x'
        column += 1
        a += 1
        b -= 1
    print 'x' * row

        
