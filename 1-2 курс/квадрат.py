row = input('������ �����: ')
column = 0
if row == 0:
    print '�������� �� ����� ���� ����������.'
if row == 1:
    print 'x'
if row > 1:
    print 'x' * row
    while column != row - 2:
        print 'x' + ' ' * (row - 2) + 'x'
        column += 1
    print 'x' * row

