
from DataStructures.BinarySearchTreeDS.BinarySearchTree import BST

bst = BST()

bst.insert(12)
bst.insert(10)
bst.insert(-2)
bst.insert(1)

bst.traverse_in_order()

bst.remove(10)

bst.traverse_in_order()

print(bst.get_max())
print(bst.get_min())

