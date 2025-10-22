# Python code to find level of a Node in Binary Tree

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Recursive function to find the level of the target key
def getLevel(root, target, level):
    if root is None:
        return -1

    # If the target key matches the current node's
    # data, return the level
    if root.data == target:
        return level

    # Recursively call for left and right subtrees
    leftLevel = getLevel(root.left, target, level + 1)
    if leftLevel != -1:
        return leftLevel

    return getLevel(root.right, target, level + 1)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    target = 5
    print(getLevel(root, target, 1))