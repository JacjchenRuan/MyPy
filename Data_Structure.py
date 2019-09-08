'''
#栈 LIFO
class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
s = Stack()
print(s.isEmpty())
s.push(1)
s.push('two')
s.push(True)
print(s.size())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.size())
'''
"""
#队列 FIFO
class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.insert(0,item)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
q = Queue()
print(q.isEmpty())
q.push(1)
q.push('two')
q.push(True)
print(q.size())
print(q.peek())
q.pop()
print(q.size())
print(q.peek())
"""
'''
#单链表
class Node():
    def __init__(self,value):
        self.value = value
        self.nextNode = None
a = Node(1)
b = Node(2)
c = Node(3)
a.nextNode = b
b.nextNode = c
print(a.nextNode.nextNode.value)
'''
'''
#双链表
class Dnode():
    def __init__(self,value):
        self.value = value
        self.next_node = None
        self.prev_node = None
a = Dnode(1)
b = Dnode(2)
c = Dnode(3)
d = Dnode(4)
a.next_node = b
b.next_node = c
c.next_node = d
b.prev_node = a
c.prev_node = b
d.prev_node = c
print(a.next_node.next_node.next_node.value)
print(d.prev_node.prev_node.prev_node.value)
'''
'''
#双端队列
class Dqueue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop(0)
    def peekFront(self):
        return self.items[0]
    def addRear(self,item):
        self.items.append(item)
    def removeRear(self):
        return self.items.pop()
    def peekRear(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
d = Dqueue()
print(d.isEmpty())
d.addFront(1)
d.addFront('two')
d.addFront(True)
print(d.peekFront())
print(d.peekRear())
d.removeRear()
d.removeFront()
print(d.items)
'''
'''
#二叉树
def BinaryTree(root):
    return [root,[],[]]
def insertLeft(tree,newBranch):
    t = tree.pop(1)
    tree.insert(1,[newBranch,t,[]])
    return tree
def insertRight(tree,newBranch):
    t = tree.pop(2)
    tree.insert(2,[newBranch,[],t])
    return tree
def getRootVal(tree):
    return tree[0]
def setRootVal(tree,newVal):
    tree[0] = newVal
def getLeftChild(tree):
    return tree[1]
def getRightChild(tree):
    return tree[2]
t = BinaryTree(0)
print(t)
insertLeft(t,1)
insertRight(t,2)
print(t)
insertRight(t,4)
print(t)
print(getRightChild(t[2]))
'''
'''
#二叉树
class BinaryTree():
    def __init__(self,rootObj):
        self.root = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self,newBranch):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newBranch)
        else:
            t = BinaryTree(newBranch)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRight(self,newBranch):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newBranch)
        else:
            t = BinaryTree(newBranch)
            t.rightChild = self.rightChild
            self.rightChild = t
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild
    def setRootVal(self,newRootObj):
        self.root = newRootObj
    def getRootVal(self):
        return self.root
r = BinaryTree(0)
r.insertRight(2)
r.insertLeft(1)
r.leftChild.insertLeft(3)
print(r.getLeftChild().getRootVal())
print(r.getLeftChild().getLeftChild().getRootVal())
print(r)
print(r.getRootVal())
'''
'''
#有向图 G = (N,E)
from collections import OrderedDict
class Node:
    def __init__(self,num):
        self.num = num
        self.adjacent = OrderedDict()
class Graph():
    def __init__(self):
        self.nodes = OrderedDict()
    def add_node(self,num):
        self.nodes[num] = Node(num)
        return Node(num)
    def add_egde(self,source,dest,weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight
g = Graph()
g.add_egde('a','b',1)
print(g.nodes)
print(g.nodes['a'].adjacent[g.nodes['b']])
g.add_egde('b','c',2)
g.add_egde('c','a',3)
print(g.nodes)
print(g.nodes['c'].adjacent[g.nodes['a']])
'''
'''
#约瑟夫环问题
def josephus(n,m,k):
    list = []
    i = 1
    while(i<=n):
        list.append(i)
        i = i+1
    index = k + m - 2
    while(len(list)>2):
        n = len(list)
        if index>=n:
            index = index - n
        x = list.pop(index)
        index = index-1+m
        print(x)
    print(list[0])
    print(list[1])
print(josephus(41,3,1))
'''


























