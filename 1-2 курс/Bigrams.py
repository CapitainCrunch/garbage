import codecs, re
from nltk import bigrams

def gen_Bigram(text):
        arr = []
        f = codecs.open(text,'r','utf8').read()
        tokens = f.split()
        for token in tokens:
                token = token.strip('.?,!:;')
                token = token.lower()
                arr.append(token)
        mn_bigram = bigrams(arr)
        return mn_bigram
                

def collect():
        arr = []
        for a in gen_Bigram('2.txt'):
                aN = (' '.join(a))
                arr.append(aN)
        for s in gen_Bigram('3.txt'):
                sN = (' '.join(s))
                arr.append(sN)
        for d in gen_Bigram('4.txt'):
                dN = (' '.join(d))
                arr.append(dN)
        words = set(arr)
        return words
                


def out_write():
        arr = []
        fOut = codecs.open('last2.txt', 'w', 'utf-8')        
        dic = {}
        for ml in gen_Bigram('1.txt'):
                mlF = (' '.join(ml))
                arr.append(mlF)
        final = set(arr)
        end = final - collect()
        for i in end:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for x in dic:
            fOut.write(x + '#' + str(dic[x]))
            fOut.write('\r\n')
        fOut.close()
                        
out_write()
