from collections import deque 

class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None 
        
# Insert elements
def insertNode(root, data):
    
    # Check if tree is currently empty, if it is, assign a new root
    if root is None:
        root = TreeNode(data)
        return root 
    
    # Otherwise do a level order traversal until we find an empty node
    q = deque()
    q.append(root)
    
    while q:
        curr = q.popleft()
        
        if curr.left is not None:
            q.append(curr.left)
        else:
            curr.left = TreeNode(data)
            return root 
        if curr.right is not None:
            q.append(curr.left)
        else:
            curr.right = TreeNode(data)
            return root
        
        
def inorder(curr):
    if curr is None:
        return 
    inorder(curr.left)
    print(curr.data, end=' ')
    inorder(curr.right)
    
if __name__ == "__main__":
  
    # Constructing the binary tree
    #          10
    #        /    \ 
    #       11     9
    #      /      / \
    #     7      15   8
    root = TreeNode(10)
    root.left = TreeNode(11)
    root.right = TreeNode(9)
    root.left.left = TreeNode(7)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(8)

    key = 12
    root = insertNode(root, key)

    # After insertion 12 in binary tree
    #          10
    #        /    \ 
    #       11     9
    #      /  \   / \
    #     7   12 15  8
    inorder(root)