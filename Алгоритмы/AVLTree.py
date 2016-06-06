__author__ = 'Bogdan'
# encoding=utf-8


class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.height = 0

    def max_children_height(self):
        if self.leftChild and self.rightChild:
            return max(self.leftChild.height, self.rightChild.height)
        elif self.leftChild and not self.rightChild:
            return self.leftChild.height
        elif not self.leftChild and self.rightChild:
            return self.rightChild.height
        else:
            return -1

    def balance(self):
        return (self.leftChild.height if self.leftChild else -1) - (self.rightChild.height if self.rightChild else -1)


class AVLTree():
    def __init__(self):
        self.rootNode = None
        self.elements_count = 0

    def height(self):
        if self.rootNode:
            return self.rootNode.height
        else:
            return 0

#я не знаю, работает ли эта функция
    def add_as_child(self, parent_node, child_node):
        node_to_rebalance = None
        if child_node.key < parent_node.key:
            if not parent_node.leftChild:
                parent_node.leftChild = child_node
                child_node.parent = parent_node
                if parent_node.height == 0:
                    node = parent_node
                    while node:
                        node.height = node.max_children_height() + 1
                        if not node.balance() in [-1, 0, 1]:
                            node_to_rebalance = node
                            break       #нам нужен дальний от корня
                        node = node.parent
            else:
                self.add_as_child(parent_node.leftChild, child_node)
        else:
            if not parent_node.rightChild:
                parent_node.rightChild = child_node
                child_node.parent = parent_node
                if parent_node.height == 0:
                    node = parent_node
                    while node:
                        node.height = node.max_children_height() + 1
                        if not node.balance () in [-1, 0, 1]:
                            node_to_rebalance = node
                            break       #нам нужен дальний от корня
                        node = node.parent
            else:
                self.add_as_child(parent_node.rightChild, child_node)

        if node_to_rebalance:
            self.rebalance(node_to_rebalance)       #тут надо ребаланс, но я не втыкаю как его реализовать

    def insert(self, key):
        new_node = Node(key)
        if not self.rootNode:
            self.rootNode = new_node
        else:
            if not self.find(key):
                self.elements_count += 1
                self.add_as_child(self.rootNode, new_node)

    def find(self, key):
        return self.find_in_subtree(self.rootNode, key)

    def find_in_subtree(self,  node, key):
        if node is None:
            return None     #ключ не найден
        if key < node.key:
            return self.find_in_subtree(node.leftChild, key)
        elif key > node.key:
            return self.find_in_subtree(node.rightChild, key)
        else:       #ключ тот же, что и у узла
            return node


#-------------------------------------------------------------------------------------------------------------------

answer_2nd = '''
мне кажется да, так как высчитывать баланс в каждом узле в большом дереве затратнее, чем обращаться к
родителю и опираться на его данные. хотя, может быть еще быстрее хранить все данные в хэш-таблице
'''

print answer_2nd