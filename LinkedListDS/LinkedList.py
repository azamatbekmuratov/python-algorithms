from LinkedListDS.Node import Node


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.counter = 0

    # O(N)
    def traverseList(self):

        actual_node = self.head

        while actual_node.next_node is not None:
            print("%d " % actual_node.data)
            actual_node = actual_node.next_node

    # O(1)
    def insert_start(self, data):
        self.counter += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    # O(1) instead of O(N)
    def size(self):
        return self.counter

    # O(N)
    def insert_at_the_end(self, data):

        if self.head is None:
            self.insert_start(data)
            return
        self.counter += 1

        new_node = Node(data)
        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    # O(N) if head O(1)
    def remove(self, data):

        self.counter -= 1
        if self.head:
            if data == self.head.data:
                self.head = self.head.next_node
            else:
                self.head.remove(data, self.head)

