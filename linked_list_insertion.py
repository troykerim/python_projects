'''
    Linked List (singly) implementation for inserting an value at the beginning.
    
   Create a new node with a given value
   Set next pointer of the new node to the current head
   move the head to point to the new node
   Return the new head of the linked list
'''

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        
def insert_front(head,data):
    # Create a newe node with the given data
    new_node = Node(data)
    
    # Make the next pointer point to the current head 
    new_node.next = head 
    
    # Return the new node as the new head of the list
    return new_node

def print_list(head):
    # Start from the head of the list
    curr = head 
    
    while curr is not None:
        print(f"{curr.data}", end=" ")
        
        # Move to the next node
        curr = curr.next
        
    print()
    
if __name__ == "__main__":
    # Test data
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next= Node(5)
    
    print("Original Linked List: ", end=" ")
    print_list(head)
    
    print("After inserting Nodes at the front: ", end=" ")
    data = 100 
    head = insert_front(head, data)
    
    # Display list after update
    print_list(head)
    
    
    