import urllib2, re, codecs

try:
    url = u'http://www.msu.ru/entrance/address.html'
    req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"}) 
    page = urllib2.urlopen(req).read()
    page = page.decode(u'utf-8').replace(u'\n', u'').replace(u'\r', u'')
except:
    page = page.decode(u'cp1251').replace(u'\n', u'').replace(u'\r', u'')

adresses = re.findall(u'[a-z0-9\-_\.]+@[a-z0-9\-_\.]+\.[a-z]{2,3}', page)
if adresses != None:
    for adress in adresses:
        print adress

print ('Part 1')
print ('\r\n')

try:
    url = u'http://www.hse.ru/org/persons/'
    req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"}) 
    page = urllib2.urlopen(req).read()
    page = page.decode(u'utf-8').replace(u'\n', u'').replace(u'\r', u'')
except:
    page = page.decode(u'cp1251').replace(u'\n', u'').replace(u'\r', u'')

phones = re.findall(u'\+?[78](?:[-()]*\d){10}', page, flags = re.U)
if phones != None:
    for phone in phones:
        print phone
        



