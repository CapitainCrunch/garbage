#ищем чего больше ma(kes?|ing?|de?) + from|of
import re, codecs

arr=[]
k=0
kof=0
kfrom=0

f=codecs.open(u'book.txt', 'r', 'utf-8-sig')
for line in f:
    line=line.strip()
    line=line.split()
    arr+=line

for i in range (len(arr)):
        m = re.search(u'ma(kes?|ing?|de?)', arr[i])
        if m != None:
            k+=1
            m = re.search(u'of', arr[i+1])
            if m != None:
                kof+=1
            m = re.search(u'from', arr[i+1])
            if m != None:
                kfrom=+1


print kof
print kfrom
    
