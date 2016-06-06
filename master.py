def D_LDistance(s1, s2):
    s1 = '#' + s1.upper()
    s2 = '#' + s2.upper()
    m = len(s1)
    n = len(s2)

    i = False
    d = False
    s = False
    r = False

    D = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            D[i][0]=i
            D[0][j]=j


    for i in range(m):
        for j in range(n):
            dis=[0]*4
            if i == 0 or j == 0:
                continue
            dis[0] = D[i-1][j] + 1
            dis[1] = D[i][j-1] + 1
            if s1[i] != s2[j]:
                dis[2] = D[i-1][j-1] + 2
            else:
                dis[2] = D[i-1][j-1]
            if s1[i] == s2[j-1] and s1[i-1] == s2[j]:
                if s1[i] != s1[i-1] and s2[j] != s2[j-1]:
                    dis[3] = D[i-1][j-1] - 1
            if dis[3] != 0:
                D[i][j] = min(dis[0:4])
            else:
                D[i][j] = min(dis[0:3])

    print '  ',
    for l in s2:
        print l+'  ',
    print '\n'

    for i in range(m):
        print s1[i],'',
        for j in range(n):
            print (D[i][j]),' ',
        print('\n')

    print "Damerau-Levenshtein Minimum Distance:",D[m-1][n-1]
    return D[m-1][n-1]

D_LDistance('python', 'pyhton')