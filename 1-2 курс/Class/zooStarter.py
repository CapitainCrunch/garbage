from zoo import Zoo
from sozinova_class_giraffe import Giraffe

z = Zoo()
for i in range(4):
    a = Giraffe()
    a.color = '#2E4DFF'
    a.marker = '<'
    z.add_animal(a)
z.start()
