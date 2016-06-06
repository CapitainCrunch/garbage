class Node:
    # класс узла
    def __init__(self, data=u''):
        # У каждого узла есть родитель (равен None, если это корень дерева),
        # дети (массив) и содержимое (какая-то строка).
        self.parent = None
        self.children = []
        self.data = data
        
    def append_node(self, data=u''):
        # Добавить ребёнка к текущему узлу.
        childNode = Node(data) # создаём новый узел
        childNode.parent = self # указываем, что текущий узел будет его родителем
        self.children.append(childNode) # указываем, что среди детей текущего
                                        # узла будет новый узел
        return childNode

    def delete_from_tree(self, tree):
        # Удалить текущий узел из дерева tree.
        if self.parent == None and tree != None and tree.root is self:
            tree.root = None
        elif self.parent != None:
            # удаляем из родителя этого узла ссылку на него
            self.parent.children.remove(self)

    def path_to_root(self):
        # Вернуть массив узлов с путём от текущего узла до корня.
        path = [self]
        curNode = self # начинаем с текущего узла
        while curNode.parent is not None:
            path.append(curNode.parent)
            curNode = curNode.parent # добавляем текущий узел к списку и
                                     # переходим на уровень выше
        return path

    def path_to_node(self, other):
        # Вернуть массив узлов с путём от текущего узла до узла other.
        path2rootSelf = self.path_to_root()
        path2rootOther = other.path_to_root()
        # Находим пути до корня от текущего узла и от узла other.
        # Если они ведут к разным корням, то это узлы из разных деревьев,
        # и найти корень не получится:
        if path2rootSelf[-1] != path2rootOther[-1]:
            return []
        for i in range(1, min([len(path2rootSelf), len(path2rootOther)]) + 1):
            # Идём с концов обоих массивов, пока не встретим точку, в которой
            # пути начинают различаться.
            if path2rootSelf[-i] != path2rootOther[-i]:
                # Если нашли, склеиваем начальный отрезок первого пути и
                # начальный отрезок второго пути (второй в обратном порядке)
                # и тут же возвращаем то, что получилось:
                return path2rootSelf[:len(path2rootSelf) - i + 2] +\
                       path2rootOther[:len(path2rootOther) - i + 1][::-1]
        # Если мы оказались здесь, значит, один из путей полностью находится
        # внутри другого.
        if len(path2rootSelf) >= len(path2rootOther):
            return path2rootSelf[:len(path2rootSelf) - len(path2rootOther) + 1]
        else:
            return path2rootOther[:len(path2rootOther) - len(path2rootSelf) + 1]

    def leaves(self):
        # Вернуть массив листьев, достижимых из данного узла.
        if len(self.children) == 0:
            # если это лист:
            return [self]
        # Если мы оказались здесь, значит, текущий узел -- не лист.
        arrLeaves = []
        for child in self.children:
            # рекурсия
            arrLeaves += child.leaves()
        return arrLeaves
        

class Tree:
    def __init__(self):
        self.root = Node() # корень дерева

    def contains_node(self, data):
        # Сообщить, есть ли в дереве узел с содержимым data.
        nodes2look = [self.root]
        # Перебираем узлы, начиная с корня. Как только мы берём какой-то
        # узел, мы сразу добавляем к массиву узлов, которые требуется
        # проверить, всех его детей.
        for node in nodes2look:
            if node is None:
                continue
            if node.data == data:
                return True # если нашли походящий узел, сразу останавливаемся
            else:
                nodes2look += node.children
        return False # если ничего не нашли, возвращаем False

t = Tree()
t.root.data = u'Корень дерева'
x = t.root
petya = x.append_node(u'Петя')
vasya = x.append_node(u'Вася')
katya = petya.append_node(u'Катя')
tanya = petya.append_node(u'Таня')

print t.contains_node(u'Варсонофий')
print t.contains_node(u'Катя')
print u'\nПуть от Тани до корня:'
for node in tanya.path_to_root():
    print node.data
print u'\nПуть от Кати до корня:'
for node in katya.path_to_root():
    print node.data
print u'\nПуть от Кати до Пети:'
for node in katya.path_to_node(petya):
    print node.data
print u'\nПуть от Кати до Тани:'
for node in katya.path_to_node(tanya):
    print node.data
print u'\nПуть от Тани до Кати:'
for node in tanya.path_to_node(katya):
    print node.data
print u'\nПуть от Васи до Васи:'
for node in vasya.path_to_node(vasya):
    print node.data
print u'\nПуть от Васи до Тани:'
for node in vasya.path_to_node(tanya):
    print node.data
print u'\nЛистья, достижимые из Пети:'
for node in petya.leaves():
    print node.data
print u'\nЛистья, достижимые из Васи:'
for node in vasya.leaves():
    print node.data
