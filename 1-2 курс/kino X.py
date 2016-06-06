import time, os
x = 0
while x < 25:
    s = ' '
    a = s*x + 'x'
    print a
    time.sleep(0.3)
    os.system('cls')
    x += 1
