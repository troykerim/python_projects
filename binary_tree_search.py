# Python program to check if a node exists
# in a binary tree

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Function to traverse the tree in preorder
# and check if the given node exists in it
def ifNodeExists(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    # then recur on left subtree
    res1 = ifNodeExists(root.left, key)

    # node found, no need to look further
    if res1:
        return True

    # node is not found in left,
    # so recur on right subtree
    res2 = ifNodeExists(root.right, key)

    return res2

if __name__ == "__main__":
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(3)
    root.left.left.left = Node(7)
    root.left.right = Node(4)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)
    root.right = Node(2)
    root.right.left = Node(5)
    root.right.right = Node(6)

    key = 4

    if ifNodeExists(root, key):
        print("True")
    else:
        print("False")
    
    key = 25 
    if ifNodeExists(root, key):
        print("True")
    else:
        print("False")    