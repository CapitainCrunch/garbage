__author__ = 'Bogdan'
# encoding=utf-8
from random import random
C = 20
arr = [0] * C
for i in range(C):
    arr[i] = int(random()*15)
for i in range(C):
    f = True
    for j in range(C):
        if arr[i] == arr[j] and i != j:
            f = False
            break
    if f == True:
        print arr[i]