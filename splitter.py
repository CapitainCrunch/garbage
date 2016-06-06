## -*- coding: utf-8 -*-
	
import re

#test = u'Добрый день, господа! Я собрал вас здесь сегодня с тем, чтобы сообщить вам пренеприятнейшее известие... К нам едет ревизор! Еще вчера ночью мне приснился странный и пугающий сон. Но мог ли я подумать, что он станет вещим?! Мог бы? Конечно нет!'
test = u'''
Hi! I asked you to come here... Because Mary was killed.
What a pity!!! Who?!Why? We should solve this crime.
To start with, her full name - Mary-Helen Black..
Oh, and I just sent you her biography, it weighs nearly 2 Gb. without photos.
'''

## splitter
MARKS_RE = u'(\.{1,3}|!{1,3}|\?\.*?|[!\?]{2,})'
result1 = re.split(MARKS_RE + u' ', test) ## return sentences with punct. marks
## result1 = re.split(u'[\.!?]{1,}', test) ## return only sentences

for i in result1:
    print i
    
print ''

## check-out
n = 0
while n != len(result1):
    try:
        print ''.join((result1[n], result1[n+1]))
        n += 2
    except:
        print result1[n]
        break
        
## tokenizer

result2 = test.split()
for token in result2:
    token = token.strip('.,!?\"\'').lower()
    print token