#вытаскивает title из ссылок 2го уровня
import urllib2, re

url = u'http://www.xerox.com/'
req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"}) 
page = urllib2.urlopen(req).read()
page = page.decode(u'utf-8').replace(u'\n', u'').replace(u'\r', u'')

m = re.search(u'<title>(.*?)</title>', page)
if m != None:
    title = m.group(1)
else:
    title = u'Не получилось.:('

print u'Title: ' + title

urls = re.findall(u'<a href=\"(http.*?)\"', page)
if urls != None:
    for links in urls:
        try:
            request = urllib2.Request(links, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"}) 
            html = urllib2.urlopen(request).read()
            html = html.decode(u'utf-8').replace(u'\n', u'').replace(u'\r', u'')
            m = re.search(u'<title>(.*?)</title>', html)
            if m != None:
                title = m.group(1)
            else:
                title = u'Не получилось.:('
            
            print u'Title: ' + title
        except:
            continue
