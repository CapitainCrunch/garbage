# Damerau-Levenshtein Distance
# encodings = utf8
def dalev(str1, str2):

    n1, n2 = len(str1), len(str2)
    max_dis = n1 + n2
    letters = {}
    INIT_POS = 2
    ORIGIN = INIT_POS - 1 
    matrix = [ [ max_dis for i1 in range(n1 + INIT_POS) ]
               for i2 in range(n2 + INIT_POS) ]
    for i1 in range(ORIGIN, n1 + INIT_POS): matrix[1][i1] = i1 -ORIGIN
    for i2 in range(ORIGIN, n2 + INIT_POS): matrix[i2][1] = i2 -ORIGIN
    for i2 in range(INIT_POS, n2 + INIT_POS):
        temp = ORIGIN
        for i1 in range(INIT_POS, n1 + INIT_POS):
            p2 = letters.get(str1[i1-INIT_POS], ORIGIN)
            p1 = temp
            cost = 0 if str1[i1-INIT_POS] == str2[i2-INIT_POS] else 1
            if not cost: temp = i1
            elem = min( matrix[i2-1][i1] + 1,
                        matrix[i2][i1-1] + 1,
                        matrix[i2-1][i1-1] + cost,
                        matrix[p2-1][p1-1] + 1 + (i1-p1-1) + (i2-p2-1) )
            matrix[i2][i1] = elem
        letters[str2[i2-INIT_POS]] = i2
    return matrix[-1][-1]

def lev(s1, s2):
	dist = {}
	dist[0,0] = 0
	for i in range(0, len(s1) + 1):
		dist[i, 0] = i
	for j in range(0, len(s2) + 1):
		dist[0, j] = j
	for i in range(0, len(s1)):
		for j in range(0, len(s2)):
				dist[i + 1, j + 1] = min(dist[i + 1, j] + 1, dist[i, j + 1] + 1, dist[i, j] + (s1[i] != s2[j]))

	return dist[len(s1), len(s2)]

