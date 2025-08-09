'''
    Linked List implementation
    
    Search for an element in a linked list (singly)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Find if a target value is present in a linked list
def search(head,target):
    
    # Initial the current node with the head of the linked list
    curr = head
    
    # Iterate over all nodes
    while curr is not None:
        # If the current node's value is equal to the target, return True
        if curr.data == target:
            return True 
        
        curr = curr.next 
    
    # If there is no node with the target value, return false
    return False 


if __name__ == "__main__":
    head = Node(14)
    head.next = Node(22)
    head.next.next = Node(13)
    head.next.next.next = Node(40)
    
    target = 13 
    
    if search(head,target):
        print("Yes")
    else:
        print("No")
