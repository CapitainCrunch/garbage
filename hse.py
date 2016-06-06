__author__ = 'Bogdan'
#encoding=utf-8
from HTMLParser import HTMLParser
import codecs

class Person(object):
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.middle_name = ''
        self.job = ''
        self.adr = ''
        self.email = []
        self.mobile = []

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.tag = tag
    def handle_data(self, data):
        print data

if __name__ == "__main__":
    text = codecs.open('in.html', 'r', 'utf-8')
    p = MyHTMLParser()
    p.feed(text.read())
    p.close()