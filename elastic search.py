import timeit

setup = '''

def binary_search(*args):
    arr = args[0]
    key = args[1]
    imin = args[2]
    imax = args[3]
    if (imax < imin):
        print 'Array is empty'
    else:
        count = 0
        imid = (imin + imax)/2
        if arr[imid] > key:
            return binary_search(arr, key, imin, imax - 1)
        else:
            if (arr[imid] < key):
                return binary_search(arr, key, imid + 1, imax)
            else:
                count +=1
                step_frw = 1
                step_bck = 1
                while x == arr[imid + step_frw]:
                    count +=1
                    step_frw +=1
                while x == arr[imid - step_bck]:
                    count +=1
                    step_bck +=1
                return count


r = [0, 3, 5, 7, 10, 20, 28, 30, 45, 45, 45, 45, 45, 56]
x = 4
mini = 0
maxi = len(r) - 1
print binary_search(r, x, mini , maxi) '''


print sum(timeit.Timer(setup=setup).repeat(10))/10


