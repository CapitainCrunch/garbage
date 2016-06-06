__author__ = 'Bogdan'
#encoding=utf-8

#iterative
def sorted_search(arr, x):
    i = 0
    j = len(arr) - 1
    m = (i + j) / 2
    count = 0
    if i > j:
        print 'Array is empty'

    if x == arr[0] and x == arr[-1]:
        count = len(arr) + 1

    if x < arr[0] or x > arr[-1]:
        print 'There is no dat int'

    else:
        while arr[m] != x or i > j:
            m = (i + j) / 2
            if x > arr[m]:
                i = m + 1
            elif i == j:
                print 'Nothing is found'
                break
            else:
                j = m
        else:
            count += 1
            step_frw = 1
            step_bck = 1
            while x == arr[m + step_frw]:
                count +=1
                step_frw +=1
            while x == arr[m - step_bck]:
                count +=1
                step_bck +=1
    return count


#recursive
def binary_search(*args):
    arr = args[0]
    key = args[1]
    if (j < i):
        print 'Array is empty'
    else:
        count = 0
        i = 0
        j = len(arr) - 1
        m = (i + j)/2
        if arr[m] > key:
            return binary_search(arr, key, i, j - 1)
        else:
            if (arr[m] < key):
                return binary_search(arr, key, m + 1, j)
            else:
                count +=1
                step_frw = 1
                step_bck = 1
                while x == arr[m + step_frw]:
                    count +=1
                    step_frw +=1
                while x == arr[m - step_bck]:
                    count +=1
                    step_bck +=1
                return count

