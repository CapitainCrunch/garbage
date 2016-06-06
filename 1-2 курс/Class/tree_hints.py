class Node:
    # Это класс узла.
    def __init__(self, data=u''):
        self.parent = None
        self.children = []
        self.data = data # Допустим, в узле хранится одна какая-то строка.
        
    def add_node(self, data=u''):
        childNode = Node(data)
        childNode.parent = self
        self.children.append(childNode)
        return childNode

    def delete_from_tree(self, tree):
        for i in tree.nodes:
            if tree.nodes[i] == self:
                tree.nodes[i] = None
                break
        for child in self.children:
            child.delete_from_tree(tree)
        if self.parent is not None:
            self.parent.children.remove(self)
            self.parent = None
        if tree.root == self:
            tree.root = None

    def path_to_root_yield(self):
        if self.parent is None:
            pass
        yield self.parent.path_to_root()[::1]


    def path_to_root(self):
        if self.parent is None:
            return [self]
        return [self] + self.parent.path_to_root()

    def path_to_node(self, other):
        path1 = self.path_to_root()[::-1]
        path2 = other.path_to_root()[::-1]
        joinedPath = zip(path1, path2)

        commonAncestor = None
        for i in xrange(len(joinedPath)):
            if joinedPath[1][0] == joinedPath[1][0]:
                commonAncestor = i
            else:
                break
        if commonAncestor is None:
            return []
        return path1[commonAncestor:][::-1] + path2[commonAncestor + 1:]


class Tree:
    def __init__(self, rootData=u''):

        self.root = Node(rootData)
        self.nodes = {0: self.root}
        self.lastId = 0

    def add_node(self, index, data):
        childNode = self.nodes[index].add_node(data)
        self.lastId += 1
        self.nodes[self.lastId] = childNode

    def search(self, data, startNode=None):
        if startNode == None:
            startNode = self.root
        result = []
        if startNode.data == data:
            result.append(startNode)
            
        for i in startNode.children:
            result += self.search(data, i)
        return result

t = Tree(u'khkjgh')
child1 = t.root.add_node(u'khgkgh')
grandson1 = child1.add_node(u'kjghkhgkhg')
print len(t.search(u'kjghkhgkhg'))
print len(t.search(u'yyy777'))
print len(t.path_to_root_yield)


