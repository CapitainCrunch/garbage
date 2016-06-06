import codecs, os, shutil
f = codecs.open('styles.txt', 'r', 'utf-8')
for line in f:
    print line
for root, dirs, files in os.walk('.'):
    for fname in files:
        if '.mp3' in fname:
            answer = raw_input(u'В какую папку скопировать ' + fname + '? ')
            if answer == '1':
                if not os.path.exists(u'./Музыка в машину/Рок/'):
                        os.makedirs(u'./Музыка в машину/Рок/')
                try:
                    transfer(u'./Музыка в машину/Рок/')
                    print u'Файл успешно скопировался'
                except:
                    print u'У-упс. Что-то не так'
            if answer == '2':
                if not os.path.exists(u'./Музыка в машину/Рэп/'):
                        os.makedirs(u'./Музыка в машину/Рок/')
                try:
                    transfer(u'./Музыка в машину/Рэп/')
                    print u'Файл успешно скопировался'
                except:
                    print u'У-упс. Что-то не так'
            if answer == '3':
                if not os.path.exists(u'./Музыка в машину/NRG/'):
                        os.makedirs(u'./Музыка в машину/NRG/')
                try:
                    transfer(u'./Музыка в машину/NRG/')
                    print u'Файл успешно скопировался'
                except:
                    print u'У-упс. Что-то не так'
            if answer == '4':
                stil = raw_input(u'Какой это стиль? ')
                styles = codecs.open('styles.txt', 'ab', 'utf-8')
                styles.write(stil + ' - ' + len(styles))
                print u'Стиль добавлен'
                if not os.path.exists(u'/Музыка в машину/' + stil):
                    os.makedirs(u'/Музыка в машину/' + stil)
                try:
                    transfer(u'./Музыка в машину/' + stil)
                except:
                    print u'У-упс. Что-то не так'
                


def transfer(way):
    for root, dirs, files in os.walk('.'):
        for name in files:
            if '.mp3' in name:
                fullname = os.path.join(root, name)
                try:
                    shutil.copy(fullname, way + name)
                except:
                    break
