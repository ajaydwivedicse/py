class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            return
        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            count += 1
            itr = itr.next


    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                if itr.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        if self.head is None:
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                break
            itr = itr.next

    def get_last_node(self):
        if self.head is None:
            print('List is empty')
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def get_length(self):
        count = 0
        if self.head is None:
            return count
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print_forward(self):
        if self.head is None:
            print('List is empty!!!')
            return
        itr = self.head
        flstr = ''
        while itr:
            flstr += str(itr.data) + '-->'
            itr = itr.next
        print(flstr)


    def print_backward(self):
        if self.head is None:
            print('List is empty')
            return
        itr = self.get_last_node()
        blstr = ''
        while itr:
            blstr += str(itr.data) + '-->'
            itr = itr.prev
        print(blstr)


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(11)
    dll.insert_at_beginning(12)
    dll.insert_at_beginning(13)
    dll.insert_at_end(14)
    dll.insert_at_end(15)
    dll.insert_at_end(16)
    dll.insert_at_end(17)
    dll.insert_at_end(18)
    l = [1, 2, 3, 4, 5]
    dll.insert_values(l)
    print('Length of our list: ', dll.get_length())
    dll.insert_after_value(3, 50)
    dll.insert_after_value(5, 51)
    dll.insert_after_value(1, 1001)
    dll.remove_at(1)
    dll.remove_at(3)
    dll.remove_by_value(51)
    dll.remove_by_value(7)

    dll.print_forward()
    dll.print_backward()

