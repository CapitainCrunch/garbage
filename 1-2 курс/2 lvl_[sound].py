#сколько раз встречается слово "sound" в статьях, на которые ссылается статья Phonology;
import urllib2, re, codecs

url = u'http://en.wikipedia.org/wiki/Phonology'
req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"}) 
page = urllib2.urlopen(req).read()
page = page.decode(u'utf-8').replace(u'\n', u'').replace(u'\r', u'')

dic_count = 0
urls = re.findall(u'<li><a href=\"(\/.*?)\"', page)
if urls != None:
    for links in urls:
        completed_links = u'http://en.wikipedia.org' + links
        request = urllib2.Request(completed_links, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"}) 
        html = urllib2.urlopen(request).read()
        html = html.decode(u'utf-8').replace(u'\n', u'').replace(u'\r', u'')
        m = re.findall(u'\\b[Ss]ounds?\\b', html, flags = re.U)
        if m != None:
            for lex in m:
                if lex in m:
                    dic_count += 1
print dic_count               
