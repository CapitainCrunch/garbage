import codecs, os, re

def collect_files(way):
    files_names = []
    for root, dirs, files in os.walk(way):
        for x in files:
            files_names.append(x)
    return files_names


def names():
    count = 0
    for name in collect_files('.'):
        m = re.findall(u'[Р-пр-џ]+\.\\w+', name, flags = re.U)
        if m != None:
            count += 1
    print count

names()

