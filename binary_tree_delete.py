from collections import deque

# Tree Node 
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Calculate Height
def getHeight(root, h):
    if root is None:
        return h - 1
    return max(getHeight(root.left, h + 1),
               getHeight(root.right, h + 1))

# Print Level Order
def levelOrder(root):
    q = deque()
    q.append((root, 0))
    lastLevel = 0
    
    # function to get the height of tree
    height = getHeight(root, 0)

    #  printing the level order of tree
    while q:
        node, lvl = q.popleft()

        if lvl > lastLevel:
            print()
            lastLevel = lvl
        
        #  all levels are printed
        if lvl > height:
            break
         
        #  printing null nodes
        if node.data != -1:
            print(node.data, end=" ")
        else:
            print("N", end=" ")
        
        # null node has no children
        if node.data == -1:
            continue

        if node.left is None:
            q.append((Node(-1), lvl + 1))
        else:
            q.append((node.left, lvl + 1))

        if node.right is None:
            q.append((Node(-1), lvl + 1))
        else:
            q.append((node.right, lvl + 1))

# Get inorder successor (smallest in right subtree)
def getSuccessor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

# Delete a node with value x from BST
def delNode(root, x):
    if root is None:
        return root

    if root.data > x:
        root.left = delNode(root.left, x)
    elif root.data < x:
        root.right = delNode(root.right, x)
    else:
        
        # node with 0 or 1  children
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        #  Node with 2 children
        succ = getSuccessor(root)
        root.data = succ.data
        root.right = delNode(root.right, succ.data)

    return root


if  __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(18)
    levelOrder(root)
    print("\n")
    x = 15
    root = delNode(root, x)
    levelOrder(root)
