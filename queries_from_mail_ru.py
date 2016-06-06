# -*- coding:utf-8 -*-

''' выдача подсказок на запрос в поисковой системе Mail.ru '''

import urllib
import urllib2
import json

class Suggester():
    def __init__(self, keyword=None):
        if keyword is None:
            keyword = ''
        self.keyword = keyword
        self._suggestions = []
        
    def read_url(self):
        query_link = "https://suggests.go.mail.ru/sg_u?q={word}".format(word=urllib.quote(self.keyword.encode('utf-8')))
        page = urllib2.urlopen(query_link)
        text = page.read().decode('utf-8')
        return text
    
    @property
    def suggestions(self):
        if self.keyword == '':
            print 'There is no suggestions for your query.'
            return
        self._suggestions = []
        query = json.loads(self.read_url())
        for suggestion in query[u'items']:
            self._suggestions.append(suggestion[u'text'])
        return self._suggestions
    
s = Suggester()
s.keyword = raw_input(u'Введите ваш запрос: ').decode('cp1251')

if s.suggestions:
    print u'Подсказки к вашему запросу:'
    for i in s.suggestions:
        print i

