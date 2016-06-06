__author__ = 'Bogdan'
#encoding=utf-8

from lxml import etree
import re
import codecs

class Tweet():

    def __init__(self):
        self.author = ''
        self.text = ''
        self.date = ''
        self.retweets = 0

    @property
    def text(self):
        if len(self.text) > 140:
            return self.text == self.text[:139]

    @property
    def rtw(self):
        if self.retweets < 0:
            return self.retweets == 0

    def get_hashtags(self):
        hashtags = re.findall('#.*?', self.text)
        return hashtags

    def get_mentions(self):
        mentions = re.findall('@.*?', self.text)
        return mentions

    def replace(self, what, replaced):
        self.text = self.text.replace(what, replaced)
        return  self.text


def fill_tweets(fname):
    tweets = []
    authors = []
    t1 = etree.parse('in.html', etree.HTMLParser())
    root = t1.getroot()
    f = codecs.open(fname, 'r', 'utf-8')
    for el in root.iter():
        if el.tag == 'div' and 'ProfileTweet-contents' in el.attrib.values():
            t = Tweet()
            for child in el:
                if child.tag == 'p':
                    t.text = child.text
                    tweets.append(child.text)
                if 'js-tweet-details-fixer tweet-details-fixer' in child.attrib.values():
                    for ch in child:
                        if 'TwitterPhoto js-media-container' in ch.attrib.values():
                            for c in ch:
                                for atr in c.attrib.values():
                                    m = re.findall('\/\/twitter\.com\/(.*?)\/status\/', atr, flags=re.U)
                                    for i in m:
                                        t.author = i
                                        authors.append(i)

                if 'ProfileTweet-action--retweet u-hiddenVisually' in child.attrib.values():
                    for x in child:
                        for i in x:
                            m = re.search(u'(.*?) рет', i.text, flags=re.U)
                            if m != None:
                                t.retweets = m.group(1)

            date = re.findall('data-long-form="true" >\s*(.*?)</span>', f.read(), flags=re.U | re.DOTALL)
            for x in date:
                t.date = x

    filled_arr = zip(authors, tweets)
    return filled_arr
fill_tweets('in.html')





