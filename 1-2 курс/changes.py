import re, codecs

def collect_lines(fname):
    words = []
    f = codecs.open(fname, 'r', 'utf-8')
    for line in f:
        line = line.lower()
        words.append(line)
        f.close()    
    return words
        
def first_letter():
    first_letter_swapped = []
    for line in collect_lines(u'new.txt'):
        re.sub = (u'(.?)(.?)(.*?)\\b', '\\2\\1\\3', line, flags = re.U)
        first_letter_swapped.append(line)
        f.close()
    return first_letter_swapped
    
def first_last():
    first_last = []
    for line in collect_lines(u'new.txt'):
        re.sub = (u'(.?)(.*?)(.?)\\b', '\\3\\2\\1', line, flags = re.U)
        first_last.append(line)
        f.close()
    return first_last

def CVC():
    cvc = []
    for line in collect_lines(u'new.txt'):
        re.sub = (u'([צךםדרשחץפגןנכהקסלעב])[ףו‎מאûÿט‏]([צךםדרשחץפגןנכהקסלעב])\\b', '\\1û\\2', line, flags = re.U)
        cvc.append(line)
        f.close()
    return cvc

def writeOut(arr):
    fOut = (u'out.txt', 'w', 'utf-8')
    for i in arr:
        fOut.write(cvc + u'\r\n')
    f.close()


def users_choice():
    answer = 
    
