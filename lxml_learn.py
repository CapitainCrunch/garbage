__author__ = 'Bogdan'
import re

from lxml import etree


class Person(object):
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.middle_name = ''
        self.job = []
        self.adr = ''
        self.email = []
        self.mobile = ''

arr = []


t1 = etree.parse('in.html', etree.HTMLParser())
root = t1.getroot()

#print root.tag
#print root.text
#print root.tail
#print root.attrib
for el in root.iter():
    if el.tag == 'div' and 'emp-text' in el.attrib.values():
        p = Person()
        for child in el:
            if 'emp-fio' in child.attrib.values():
                for ch in child:
                    p.name = ch.text
            if 'emp-description' in child.attrib.values():
                for ch in child:
                    if 'details' in ch.attrib.values():
                        fs = ch.text
                        if fs != None:
                            finds = re.findall(u'(?<=:)[^|]+', fs)
                            for j in finds:
                                p.job.append(j)
                        else:
                            continue
                    if 'addr' in ch.attrib.values():
                        p.adr = ch.text
                    if 'tel' in ch.attrib.values():
                        p.mobile = ch.text
                    if 'text/javascript' in ch.attrib.values():
                        mail = re.sub(u'[\'\+]', u'' , ch.text)
                        mail_t = re.search(u'document.write((.*?)<wbr/>(.*?));', mail)
                        if mail_t != None:
                            mail_in = mail_t.group(2) + mail_t.group(3)
                            p.email.append(mail_in[1:-1])

        arr.append(p)
print len(arr)
