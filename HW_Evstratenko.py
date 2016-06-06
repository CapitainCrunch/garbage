#-*- coding:utf-8 -*-
 
class OldString:
    def __init__(self, text):
        self.text = text
 
    def __lt__(self, other):
        minRange = min(len(self.text), len(other.text))
        for i in range(minRange):
            selfLetter = dict[self.text[i].lower()]
            otherLetter = dict[other.text[i].lower()]
            if selfLetter > otherLetter:
                return False
            elif selfLetter == otherLetter:
                if i != minRange - 1:
                    continue
                else:
                    if len(self.text) < len(other.text):
                        return True
                    else:
                        return False
            else:
                return True
 
letters = u'АаБбВвГгДдЕеЖжЗзИиІіЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьѢѣЭэЮюЯяѲѳѴѵ'

dict = {}
count = 0
for i in letters:
    dict[i] = count
    count += 1
 
