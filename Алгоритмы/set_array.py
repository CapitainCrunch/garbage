__author__ = 'Bogdan'
from random import randint
import time
a = set()
array = []

while len(a) < 1000000:
    a.add(randint(1,11000000))


def search(st):
    start = time.clock()
    if randint(1,11000000) in st:
        end = time.clock()
        arr = [(start, end)]
        print 'True'
        return arr
    else:
        end = time.clock()
        arr = [(start, end)]
        print 'False'
        return arr

def insrt(st):
    start = time.clock()
    st.add(randint(10000000000,9000000000000))
    end = time.clock()
    arr = [(start, end)]
    return arr

def remv(st):
    start = time.clock()
    try:
        st.remove(randint(1,11000000))
        end = time.clock()
        print 'True'
        arr = [(start, end)]
        return arr
    except KeyError:
        print 'False'
        end = time.clock()
        arr = [(start, end)]
        return arr




while len(array) < 1000000:
    array.append(randint(1,11000000))


def search_array(st):
    start = time.clock()
    if randint(1,11000000) in st:
        end = time.clock()
        arr = [(start, end)]
        print 'True'
        return arr
    else:
        end = time.clock()
        arr = [(start, end)]
        print 'False'
        return arr

def insrt_array(st):
    start = time.clock()
    array.insert(randint(0, len(array)), randint(1,1100000))
    end = time.clock()
    arr = [(start, end)]
    return arr

def remv_array(st):
    start = time.clock()
    try:
        st.remove(randint(1,11000000))
        end = time.clock()
        print 'True'
        arr = [(start, end)]
        return arr
    except ValueError:
        end = time.clock()
        arr = [(start, end)]
        return arr

#s = 0
#e = 0
#for z in xrange(20):
#   for i in search(a):
  #      s += i[0]
 #       e += i[1]

#f = float(e - s)/20
#print f
