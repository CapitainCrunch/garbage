class sNode(Node):
    def __init__(self, name=None):
        self.name = name
        self.parent = None
        self.children = []


class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_node(self, node):
        node.parent = self
        self.children.append(node)

    def tree_walk(self, lvl=0, lvl_now=1):
        if lvl_now >= lvl:
            yield self
        if lvl_now != lvl:
            for child in self.children:
                for res in child.tree_walk(lvl, lvl_now+1):
                    yield res


    def get_nodes(self, req):
        arr = []
        def accessory_func(node, req, srch):
            if node.name == req:
                arr.append(node)
            for i in node.children:
                accessory_func(i, req, srch)
        accessory_func(self, req, srch)
        return arr




