# This file contains my implementation of linked list with end node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class MyList:
    def __init__(self):
        self.firstnode = None
        self.lastnode = None

    def isempty(self):
        return self.firstnode is None

    def getdata(self, node):
        return node.data

    def frontdata(self):
        return self.firstnode.data

    def backdata(self):
        return self.lastnode.data

    def push_back(self, data):
        node = Node(data, None)
        if self.isempty():
            self.firstnode = node
            self.lastnode = node
            return
        self.lastnode.next = node
        self.lastnode = node

    def push_front(self, data):
        node = Node(data, self.firstnode)
        if self.isempty():
            self.firstnode = node
            self.lastnode = node
            return
        node.next = self.firstnode
        self.firstnode = node

    def pop_back(self):
        if self.isempty():
            print('List is empty!!!')
            return
        if self.firstnode == self.lastnode:
            self.firstnode = None
            self.lastnode = None
            return
        itr = self.firstnode
        while itr.next:
            if itr.next == self.lastnode:
                self.lastnode = itr
                self.lastnode.next = None
                return
            itr = itr.next



    def pop_front(self):
        if self.isempty():
            print('List is empty!!!')
            return
        if self.size() == 1:
            self.firstnode = None
            self.lastnode = None
            return
        self.firstnode = self.firstnode.next


    def traverse(self):
        if self.isempty():
            print('List is empty!!!')
            return
        itr = self.firstnode
        mlstr = ''
        while itr:
            data = self.getdata(itr)
            mlstr += str(data) + '==>'
            itr = itr.next
        print(mlstr)

    def size(self):
        count = 0
        if self.isempty():
            return count
        itr = self.firstnode
        while itr:
            count += 1
            itr = itr.next
        return count

if __name__ == '__main__':
    ml = MyList()
    ml.push_front(1)
    ml.push_back(2)
    ml.push_back(3)
    ml.traverse()
    print(ml.size())
    ml.pop_front()
    ml.traverse()
    ml.pop_front()
    ml.traverse()
    ml.pop_front()
    ml.traverse()

