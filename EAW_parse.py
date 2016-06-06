__author__ = 'Bogdan'
# encoding=utf-8
import os
import re


first_names = ['abdurashitova', 'Bobrova', 'Bolgina', 'Bruskova',
               'Emelyanova', 'Ershova', 'Garkavaya', 'Kasinceva',
               'Katelzyan', 'Kazakova', 'Kolomeycev', 'Kovalevskaya',
               'Leenson', 'Miheeva', 'Mozhaev', 'Naletova', 'Nikishina',
               'Obedkova', 'Safonova', 'Saveleva', 'Shakurova', 'Tolkacheva',
               'Vasilisina', 'Vishenkova', 'Vyunova', 'Yakubovskaya', 'Zarifyan']

from_file = []

for root, dirs, files in os.walk('/Users/Bogdan/Desktop/EAW/HW2'):
    #print len(files)
    for file in files:
       # print file
        from_file.append(file.lower())

for names in from_file:
    #print names
    n = re.findall('....(\w+.*?).graded.(\d\.?\d?)', names.lower(), flags=re.U)
    for name in n:
        print sorted(name,key=lambda x: x[0])
