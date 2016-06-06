__author__ = 'Bogdan'
#encoding=utf-8

from lxml.html import parse
import codecs, re

class Person(object):
    def __init__(self):
        self.name = ''
        self.job = []
        self.adr = ''
        self.email = []
        self.mobile = ''

arr = []
text = codecs.open('in.html', 'r', 'utf-8')
data = parse(text)

for pers in data.findall('//*[@class="emp-text"]'):
    p = Person()
    children = pers.getchildren()
    p.name = (''.join([x for x in children[0].itertext()]))
    details =  children[1].getchildren()
    for number, detail in enumerate(details):
        if number == 0:
            work =  ''.join([x for x in detail.itertext()])
            if work != None:
                finds = re.findall(u'(?<=:)[^|]+', work)
                for j in finds:
                    p.job.append(j)
            else:
                continue
    adr = pers.xpath('.//*[@class="addr"]')
    if len(adr) > 0:
        p.adr = adr[0].text[7:]
    else:
        p.adr = ''
    number = pers.xpath('./div/p[@class="tel"]')
    if len(number) > 0:
        p.mobile = number[0].text[9:]
    else:
        p.mobile = ''
    mail = pers.xpath('./div/script[@type="text/javascript"]')
    if len(mail) > 0:
        mail = re.sub(u'[\'\+]', u'' ,mail[0].text)
        mail_t = re.search(u'document.write((.*?)<wbr/>(.*?));', mail)
        if mail_t != None:
            mail_in = mail_t.group(2) + mail_t.group(3)
            print mail_in
            p.email.append(mail_in[1:-1])
    arr.append(p)


