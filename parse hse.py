import codecs, re

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
f = codecs.open(u'in.html', 'r', 'utf-8')
f = f.read()
m = re.findall(u'<div class=\"emp-fio\">(.*?)<div class="emp-text">', f, flags=re.U | re.DOTALL)
for pers in m:
    p = Person()
    
    info = re.search(u'<a href="http://www.hse.ru/.*(\w+)\s(\w+)\s(\w*)</a>', pers, flags=re.U)
    if info != None:
        p.surname = info.group(1)
        p.name = info.group(2)
        p.middle_name = info.group(3)

    j = re.search(u'<p class="details">(.*? \|.*?\: (.*?))\s\|\s(.*? \|.*?\: (.*?))?\s\|\s(.*? \|.*?\: (.*?))?</p>', pers, flags=re.U)
    if j != None:
        p.job.append(j.group(2))
        p.job.append(j.group(4))
        p.job.append(j.group(6))

    addr = re.search(u'<p class="addr">.*?: (.*?)</p>', pers, flags=re.U)
    if addr != None:
        p.adr = addr.group(1)

    mail = re.search(u'</script>(.*?)<wbr>(.*?)(; (.*?)<wbr>(.*?))?</p>', pers, flags=re.U)
    if mail != None:
        emails = mail.group(1) + mail.group(2)
        p.email.append(emails)
        try:
            emails2 = mail.group(4) + mail.group(5)
            p.email.append(emails2)
        except:
            pass

    mob = re.search(u'<p class="tel">Телефон: (.*?)</p>', pers, flags=re.U)
    if mob != None:
        p.mobile = mob.group(1)
    arr.append(p)



print arr