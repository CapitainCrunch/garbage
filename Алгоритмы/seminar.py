__author__ = 'Bogdan'
# encoding=utf-8




def second():
    #Найти максимальную по длине возрастающую подпоследовательность в массиве
    sequence = [1, 2, 3, -5, -4, -3, -2, -1]
    lengths = []
    for i, s in enumerate(sequence):
        if i == 0:
            lengths.append(1)
        else:
            possibles = []
            for j, length in enumerate(lengths):
                if s > sequence[j]:
                    possibles.append(length + 1)
                    print possibles
                else:
                    possibles.append(1)
            lengths.append(max(possibles))

