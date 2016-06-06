''' выдача подсказок из разных сервисов Mail.ru, разных сервисов Яндекса и Википедии на русском и английском языках '''
#encoding=utf-8
import urllib
import urllib2
import json

TITLES = {u'Яндекс.Новости':"http://suggest.yandex.ru/suggest-news-ru?part={word}",
          u'Яндекс.Маркет':"http://suggest-market.yandex.ru/suggest-market?part={word}",
          u'Яндекс.Картинки':"http://suggest-images.yandex.ru/suggest-ya.cgi?part={word}",
          u'Яндекс.Видео':"http://suggest-video.yandex.ru/suggest-ya.cgi?part={word}",
          u'Мэил.Поиск':"https://suggests.go.mail.ru/sg_u?q={word}",
          u'Мэил.Картинки':"http://suggests.go.mail.ru/sg_images_u?q={word}",
          u'Мэил.Обсуждения':"http://suggests.go.mail.ru/sg_realtime_u?q={word}",
          u'Википедия.Англ':"http://en.wikipedia.org/w/api.php?action=query&format=json&list=prefixsearch&pssearch={word}&pslimit={number}",
          u'Википедия.Рус':"http://ru.wikipedia.org/w/api.php?action=query&format=json&list=prefixsearch&pssearch={word}&pslimit={number}"}

class Suggester():
    ''' класс основного Suggester'а, по умолчанию массив с подсказками пуст '''
    def __init__(self, keyword=None):
        if keyword is None:
            keyword = ''
        self.keyword = keyword
        self._suggestions = []

    def read_url(self):
        query_link = TITLES[chosen_system].format(word=urllib.quote(self.keyword.encode('utf-8')))
        page = urllib2.urlopen(query_link)
        text = page.read().decode('utf-8')
        return text

    @property
    def suggestions(self):
        if self.keyword == '':
            print 'There is no suggestions for your query.'
            return []
        self._suggestions = []
        return self._suggestions

class YandexSuggester(Suggester):
    ''' класс-наследник Suggester'а для сервисов Яндекса;
    проверка на наличие suggest.apply() актуальна для сервисов Яндекс.Новости и Яндекс.Видео
    (suggest.apply() возникает при избавлении от jQuery и ненужных аргументов в строке запроса) '''
    def read_url(self):
        query_link = TITLES[chosen_system].format(word=urllib.quote(self.keyword.encode('utf-8')))
        page = urllib2.urlopen(query_link)
        text = page.read().decode('utf-8')
        # последовательность ',[])' возникает после jSon объекта при наличии suggest.apply()
        if text.startswith('suggest'):
            text = text.replace('suggest.apply(', '')[:-len(',[])')]
        return text

    @property
    def suggestions(self):
        if self.keyword == '':
            print 'There is no suggestions for your query.'
            return []
        self._suggestions = []
        query = json.loads(self.read_url())
        if len(query) > 1:
            for suggestion in query[1]:
                self._suggestions.append(suggestion)
        return self._suggestions

class MailSuggester(Suggester):
    ''' класс-наследник Suggester'а для сервисов Мэила '''
    @property
    def suggestions(self):
        if self.keyword == '':
            print 'There is no suggestions for your query.'
            return []
        self._suggestions = []
        query = json.loads(self.read_url())
        try:
            if len(query[u'items']) < 1:
                print 'There is no suggestions for your query.'
            for suggestion in query[u'items']:
                try:
                    self._suggestions.append(suggestion[u'text'])
                except KeyError:
                    print 'There is no suggestions for your query.'
        except KeyError:
            print 'There is no suggestions for your query.'
        return self._suggestions

class WikiSuggester(Suggester):
    ''' класс-наследник Suggester'а для русской и английской Википедии;
    помимо запроса в виде символьной последовательности можно менять количество выдаваемых подсказок '''
    def read_url(self):
        query_link = TITLES[chosen_system].format(word=urllib.quote(self.keyword.encode('utf-8')), number=amount_of_suggestions)
        page = urllib2.urlopen(query_link)
        text = page.read().decode('utf-8')
        return text
    
    @property
    def suggestions(self):
        if self.keyword == '':
            print 'There is no suggestions for your query.'
            return []
        self._suggestions = []
        query = json.loads(self.read_url())
        try:
            if len(query[u'query'][u'prefixsearch']) < 1:
                print 'There is no suggestions for your query.'
            for suggestion in query[u'query'][u'prefixsearch']:
                try:
                    self._suggestions.append(suggestion[u'title'])
                except KeyError:
                    print 'There is no suggestions for your query.'
        except KeyError:
            print 'There is no suggestions for your query.'
        return self._suggestions
    
def choose_search_system():
    ''' функция для выбора системы поиска;
    стоит проверка при введении названия системы;
    в зависимости от выбранной системы (Яндекс/Мэил/Вики), меняется базовый класс объекта на соответствующий выбору;
    для объекта класса WikiSuggester стоит проверка на количество запрашиваемых подсказок '''
    print u'Выберите систему, в которой хотите начать поиск:'
    for title in sorted(TITLES):
        print title
            
    global chosen_system
    chosen_system = raw_input(u'Введите название выбранной системы: ').decode('cp1251')
    while chosen_system not in TITLES:
        chosen_system = raw_input(u'Введите название выбранной системы: ').decode('cp1251')
    if chosen_system.startswith(u'Яндекс'):
        s = YandexSuggester()
    elif chosen_system.startswith(u'Мэил'):
        s = MailSuggester()
    elif chosen_system.startswith(u'Вики'):
        s = WikiSuggester()
        global amount_of_suggestions
        amount_of_suggestions = raw_input(u'Введите количество подсказок, которое хотите получить: ')
        while not amount_of_suggestions.isdigit() or int(amount_of_suggestions) < 1:
            amount_of_suggestions = raw_input(u'Введите количество подсказок, которое хотите получить: ')
    return s, chosen_system

def check_keyword(word):
    ''' проверка вводимого запроса на наличие знаков препинания в нём '''
    symbols = list('.,?!-:;')
    while any(symb in word for symb in symbols):
        word = raw_input(u'Введите ваш запрос: ').decode('cp1251')
    return word

s, chosen_system = choose_search_system()

print

s.keyword = check_keyword(raw_input(u'Введите ваш запрос: ').decode('cp1251'))

print u'Подсказки по вашему запросу:'
for i in s.suggestions:
    print i
