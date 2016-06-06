__author__ = 'Bogdan'
# encoding=utf-8
import os

word = ''
word_length = 0
max_steps = word_length * 2 - 1
start_symbol = 'S' # поменять, если надо
productions = {} # сюда словарь
table = [] # хранить вычисления

def find_productions(list1, list2):
    global productions

    new_list = []

    if not list1 or not list2: return new_list

    for x in list1:
        for y in list2:
            for i in productions:
                for j in range(0, len(productions[i])):
                    if x + y == productions[i][j] and i not in new_list:
                        new_list.append(i)
    return new_list


def grammar_check():
    # я знаю, что это плохо, но...
    global word
    global table
    global productions
    global word_length

    #создаем табличку
    for i in xrange(0, word_length):
        table.append([])
        for j in xrange(0, word_length):
            table[i].append([])

    # вставляем 1 терминальный символ в диагональ
    for i in xrange(0, word_length):
        for j in productions:
            for symbols in productions[j]:
                if symbols == word[i]:
                    table[i][i].append(j)
                    continue

    #да начнется магия
    for k in xrange(1, word_length):
        for j in xrange(k, word_length):  # первые два цикла проходят по пустым ячейкам
            for l in xrange(j-k, j):  # третий цикл - колво ячеек откуда считать и сами ячейки
                for list_item in find_production(table[j-k][l], table[l+1][j]):  # выбираем терминальный символ и находим соответствующий квадрат
                    if list_item not in table[j-k][j]:  # место где есть неповторяющиеся символы в текущей ячейке
                        table[j-k][j] += list_item

    print table

    if start_symbol in table[0][word_length - 1]: return True
    else: return False

