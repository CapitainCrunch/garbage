import urllib2, re

# Скачать главную страницу ленты.ру
url = 'http://lenta.ru/'
req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"}) 
page = urllib2.urlopen(req).read()
page = page.decode(u'utf-8').replace(u'\n', u'').replace(u'\r', u'')
# (такие сложности -- на всякий случай, чтобы обойти возможные ограничения
# на загрузку страницы ботами)

# Вытащить из HTML'а главный заголовок новости
m = re.search(u'>([^<]*)</a></h2>', page)
if m != None:
    headline = m.group(1)
else:
    headline = u'Не получилось.:('

# Скачать страницу Яндекс.Погоды
url = 'http://pogoda.yandex.ru/moscow'
req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"}) 
page = urllib2.urlopen(req).read()
page = page.decode(u'utf-8').replace(u'\n', u'').replace(u'\r', u'')

# Вытащить из HTML'а сегодняшнюю температуру и облачность
m = re.search(u'<div class="b-thermometer__now">([^<]*)</div>.*?'
              u'<div class="b-info-item b-info-item_type_fact-big">([^<]*)</div>', page)
if m != None:
    weather = m.group(1) + u', ' + m.group(2)
else:
    weather = u'Не получилось с погодой.:('

print u'Headline: ' + headline
print u'Weather: ' + weather

# ВСЁ!





