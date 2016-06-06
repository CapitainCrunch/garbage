class Tree:
    def __init__(self):
        #just for being
        self.name = 'Old Tree'

class Node:
    def __init__(self, name):
        self.parent = None
        self.name = name
        self.children = []
    
    def hook_nodes(self, value, arr=[]):
        if self.name == value:
            arr.append(self)
        for i in self.children:
            i.hook_nodes(query, arr)
        return arr

    def talk(self):
        try:
            x = x.talk()
            for x in self.children:
                return self.name + '---' + ', '.join(x)
        except:
            return self.name

    def insert_node(self, node):
        self.children.append(node)
        node.parent = self
        return node

class scndTree(Tree):
    def __init__(self):
        self.name = 'New Tree'

class scndNode(Node):
    def __init__(self, name=''):
        self.children = []
        self.name = name
        self.parent = None

    def hook_children(self):
        return self.children

    def hook_old(self, k):
        old = self
        for i in range(k):
            if old != None:
                old = old.parent
            else:
                pass
        return old


