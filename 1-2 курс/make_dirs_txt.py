#В первой папке создать текстовые файлы с номерами от 1 до n, во втором -- от 2 до n + 1 и т. д.
import codecs, os

n = input('Input a number: ')

root = 1
while root <= n:
    if not os.path.exists(str(root)):
        os.makedirs(str(root))
    row = n + 1
    while row >= root:
        f = codecs.open(u'./' + str(root) + u'\\' + str(row) + '.txt','w',u'utf-8')
        row -= 1
    root += 1
    


