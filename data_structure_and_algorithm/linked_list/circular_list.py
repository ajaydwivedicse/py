"""
####Questions####
1. Find the mid-point of a linked list, assuming you are not allowed to modify the data
structure and then solve it again assuming you are allowed to modify the data structure.
2. Find if a linked list has a cycle using constant space and in O(n) steps.
3. Reverse a singly linked list using O(1) memory space.
4. A linked list contains only one element which is a duplicate. Find it in O(n) steps.
5. Implement a linked list which supports O(1) time delete operation for the entire list.
6. Given two sorted linked lists, merge them to create a single linked list which is sorted.
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data, self.head)
        if self.head is None:
            self.head = node
            node.next = self.head
            return

        itr = self.head
        while itr.next != self.head:
            itr = itr.next
        itr.next = node
      #  node.next = self.head

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def get_length(self):
        count = 0
        if self.head is None:
            return count
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def print_all(self):
        if self.head is None:
            print("Linked list is empty!!!")
            return
        llstr = ''
        itr = self.head
        while True:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
            if itr == self.head:
                break

        llstr += '(back to head)'
        print(llstr)

    # Find the mid-point of a linked list, assuming you are not allowed to modify the data structure
    def get_mid(self):
        if self.head is None:
            print("Linked list is empty!!!")
            return
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def is_cycle(self):
        if self.head is None:
            print('Linked list is empty!!!')
            return False
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True


        return False


if __name__ == '__main__':
    ll = LinkedList()
    #    ll.insert_values(["banana", "mango", "grapes", "orange"])
    #   ll.print_all()
    # ll.insert_after_value("mango", "apple")  # insert apple after mango
    #   print('Mid point: ', ll.get_mid())
    ll.insert_at_end(10)
    ll.insert_at_end(100)
    ll.insert_at_end(1000)
    ll.insert_at_end(10000)
    ll.insert_at_end(100000)
    print(ll.is_cycle())

    ll.print_all()
