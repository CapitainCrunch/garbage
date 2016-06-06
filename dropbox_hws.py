import shutil
import os
PATH = '/Users/Bogdan/Desktop/HW1'

SURNAMES = [u"151_Astafeva", '151_Yatsyk', '151_Bagryanskaya', u"151_Grigoreva", u'151_Zueva', u'151_Kireeva',
            u'151_Kozenasheva', u'151_Koshevoj', u'151_Levakova', u'151_Pinigina', u"151_Sinelnik",
            u'151_Sokur', u'151_Trublovskaja', u'151_Bagdasarjan', u'151_Vodovatova', u'151_Kazakova',
            u'151_Kamilova', u'151_Kim', u'151_Lukancova', u'151_Masumi', u'151_Nedolivko',
            u'151_Orlenko', u'151_Petuhova', u'151_Smirnova', u'152_Aleksandrova',
            u'152_Borisov', u'152_Gajan', u'152_Ginazova', u'152_Drozdova', u'152_Klezovich',
            u'152_Miller', u'152_Mihajlov', u'152_Panteleeva', u'152_Rudina', u'152_Slepak',
            u'152_Sokolovskij', u'152_Timoshina', u'152_Frolov', u'152_Cyzova', u'152_Voronov',
            u'152_Kopeckij', u'152_Lapin', u'152_Matveeva', u'152_Myslina', u'152_Popkova',
            u'152_Romanova', u'152_Savinova', u'152_Simonjan', u'152_Tatarinov', u'152_Fedorenko',
            u'152_Hristosova',u'153_Golosov', u'153_Ermolaeva', u'153_Zdorova',
            u'153_Ivanova', u'153_Kovaleva', u"153_Kondrateva", u'153_Makarovich', u'153_Metelkina',
            u'153_Ovchinnikova', u'153_Careva', u'153_Shajmardanova', u'153_Belyh', u'153_Glazunova',
            u'153_Durneva', u'153_Kozlov', u'153_Kostjanicyna', u'153_Kosheleva', u'153_Lunina',
            u'153_Maksimova', u'153_Mizerova', u'153_Miljaeva', u'153_Panova', u'153_Sattarova',
            u'153_Ushkalova']



def collect():
    unit = input('Which unit is dwnlded? 1? 2?... ' )
    group = input('Which group is dwnlded? 151? 152? 153? ' )
    for surname in SURNAMES:
        to_path = PATH + '/' + group + '_Unit' + unit + '/' + surname

        from_path = PATH + '/' + surname + '/Unit' + unit
        print(from_path)
        try:
            shutil.copytree(from_path, to_path)
        except:
            pass




def count():
    c = 0
    for surname in SURNAMES:
        from_path = PATH + '/' + surname
        for root, dirs, files in os.walk(from_path):
            if root.endswith('LiveCorpus') or root.endswith('Unit1') or root.endswith('Unit5') or root.endswith('Unit7') or root.endswith('Unit9'):
                continue
            if files != []:
                c+=1
        print(surname + '\t' + str(c))
        c = 0


count()