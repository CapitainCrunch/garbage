__author__ = 'Bogdan'

class Stack(object):
    def __init__(self, size=8):
        self.stack = []
        self.size = size
        self.top = -1

    def set_size(self, size):
        if self.top >= size:
            raise Exception("StackWillOverFlow")
        self.size = size

    def is_full(self):
        return True if self.size == self.top + 1 else False

    def is_empty(self):
        return True if self.top == -1 else False

    def push(self, data):
        if self.is_full():
            raise Exception("StackOverFlow")
            return
        self.stack.append(data)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception("StackIsEmpty")
            return
        self.top -= 1
        return self.stack.pop()

s = Stack()
for i in xrange(8):
    s.push(i)
print s.stack
s.pop()
s.pop()
print s.stack


class Queue(object):
    def __init__(self, size = 8):
        self.queue = []
        self.size = size
        self.front = 0
        self.rear = -1

    def is_full(self):
        return True if self.rear == self.size - 1 else False

    def is_empty(self):
        return True if self.rear == -1 else False

    def enqueue(self, data):
        if self.is_full():
            raise Exception("QueueOverFlow")
        self.queue.append(data)
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("QueueIsEmpty")
        self.rear -= 1
        return self.queue.pop(self.front)

q = Queue()
print 'Queue'
for i in xrange(8):
    q.enqueue(i)
print q.queue
q.dequeue()
print q.queue