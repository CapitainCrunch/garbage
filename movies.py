__author__ = 'Bogdan'
#encoding=utf-8

import re, urllib2
from datetime import *
from lxml import etree

class Movie(object):
    def __init__(self):
        self.name = ''
        self.href = ''
        self.genre = ''
        self.description = ''

year = str(2013)
#year = raw_input('Year: ')
sys_year = str(datetime.now())[:4]
if int(year) > int(sys_year):
    print 'Error'

arr = []
for page in xrange(1, 50):
    url = 'http://kinogo.net/filmy_' + year + '/page/' + str(page) + '/'
    req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0"})
    page = urllib2.urlopen(req)
    t1 = etree.parse(page, etree.HTMLParser())
    root = t1.getroot()
    for el in root.iter():
        if el.tag == 'h2':
            m = Movie()
            for e in el:
                 for href in e.attrib.values():
                    m.href = href
            for i in el:
                m.text = i.text
            arr.append(m)

for i in arr:
    print i.text
    print i.href
    print ('\r\n')

    #solarisк858рк190