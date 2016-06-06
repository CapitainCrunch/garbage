__author__ = 'Bogdan'
# encoding=utf-8

def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for _ in xrange(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    lcs_w = s1[x_longest - longest: x_longest]
    return lcs_w, len(lcs_w)

print longest_common_substring('feed', 'ed')

#O(n*m) - сложность
#должны пройтись по "табличке", которая у меня лежит в переменной m.
#она размером как раз m*n