__author__ = 'Bogdan'
import os, shutil
arr = ['Sasha', 'Ivan', 'Bogdan']
try:
    for mname in arr:
        os.makedirs('./' + mname)
except:
    pass

for root, dirs, files in os.walk(u'./HW'):
    sasha = files[::3]
    ivan = files[1::3]
    bogdan = files[2::3]
    for i in sasha:
        shutil.move('./HW/' + i, './Sasha/' + i)
    for z in ivan:
        shutil.move('./HW/' + z, './Ivan/' + z)
    for x in bogdan:
        shutil.move('./HW/' + x, './Bogdan/' + x)


