#самое длинное слово в тхт файле
import codecs



f = codecs.open(u'1.txt', 'r', 'utf-8')
words = []
for line in f:
    words += line.split()

longest_word = ''
for i in words:
    if len(i) > len(longest_word):
        longest_word = i
        

print longest_word

f.close()
