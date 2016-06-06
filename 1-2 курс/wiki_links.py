import codecs, re

def find_wiki_links(text):
    # функция находит в html, содержащемся в строке text,
    # все ссылки на статьи в википедии,
    # каждая ссылка представляет собой кортеж из названия статьи,
    # на которую ведёт ссылка, и слова, которое является ссылкой
    text = text.replace(u'\r', u'').replace(u'\n', u'')
    links = re.findall(u'<a\\s+href\\s*=\\s*"/wiki/[^"]*"\\s+'
                       u'title\\s*=\\s*"([^"]+)"[^>]*>'
                       u'([^<>]+)</a>', text)
    return links


def main(filename):
    f = codecs.open(filename, 'r', 'utf-8-sig')
    links = find_wiki_links(f.read())
    f.close()

    f_csv = codecs.open(u'links.csv', 'w', 'utf-8')
    for link in links:
        f_csv.write(link[0] + u';' + link[1] + u'\r\n')
    f_csv.close()
    print u'Записано ссылок: ' + str(len(links)) + u'.'


if __name__ == u'__main__':
    main(u'page.html')
