import os

def make_dirs():
    try:
        for x in range(1, 5):
            os.makedirs(str(x))
            for y in range(1, 5):
                os.makedirs('C:\\Users\\student\\Desktop\\' + str(x) + u'\\' + str(y))
    except OSError:
        pass

make_dirs()

