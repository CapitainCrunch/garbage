import urllib, urllib2, json
y=raw_input(u'Введите запрос' )
print urllib.quote(y)
page=urllib2.urlopen('http://suggest.yandex.ru/suggest-ya.cgi?srv=morda_ru&wiz=TrWth&lr=213&uil=ru&fact=1&v=4&icon=1&hl=1&html=1&yu=1350190401418998070&pos=1&part='+urllib.quote(y)+'&_=1418998259807')
page2=urllib2.urlopen('http://suggest.yandex.ru/suggest-ya.cgi?srv=morda_ru&wiz=TrWth&lr=10725&uil=ru&fact=1&v=4&icon=1&hl=1&html=1&yu=7774767161419444924&pos=2&part=' + urllib2.quote(y) + '&_=1419445165763')
text=page.read().decode(u'utf-8')
x=json.loads(text)

for q in x[1]:
    print q[1]

