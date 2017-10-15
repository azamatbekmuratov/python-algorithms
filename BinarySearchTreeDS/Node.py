

class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data)
            else:
                self.leftChild.insert(data)
        else:
            if not self.rightChild:
                self.rightChild = Node(data)
            else:
                self.rightChild.insert(data)

    def remove(self, data, parent_node):

        if data < self.data:
            if self.leftChild is not None:
                self.leftChild.remove(data, self)
        elif data > self.data:
            if self.rightChild is not None:
                self.rightChild.remove(data, self)
        else:
            if self.leftChild is not None and self.rightChild is not None:
                self.data = self.rightChild.get_min()
                self.rightChild.remove(self.data, self)
            elif parent_node.leftChild == self:
                if self.leftChild is not None:
                    temp_node = self.leftChild
                else:
                    temp_node = self.rightChild

                parent_node.leftChild = temp_node

            elif parent_node.rightChild == self:
                if self.leftChild is not None:
                    temp_node = self.leftChild
                else:
                    temp_node = self.rightChild

                parent_node.rightChild = temp_node

    def get_min(self):
        if self.leftChild is None:
            return self.data
        else:
            return self.leftChild.get_min()

    def get_max(self):
        if self.rightChild is None:
            return self.data
        else:
            return self.rightChild.get_max()

    def traverse_in_order(self):
        if self.leftChild is not None:
            self.leftChild.traverse_in_order()

        print(self.data)

        if self.rightChild is not None:
            self.rightChild.traverse_in_order()





