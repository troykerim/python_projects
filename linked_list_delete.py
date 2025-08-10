'''
    Linked List (singly) implementation for deleting a value at the beginning.
    
   Create a new node with a given value
   Set next pointer of the new node to the current head
   move the head to point to the new node
   Return the new head of the linked list
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def delete(head):
    if head is None:
        return None 
    temp = head 
    head = head.next 
    del temp
    
    return head 

def print_list(curr):
    while curr:
        print(curr.data, end=" ")
        curr = curr.next 
    print()
        
if __name__ == "__main__":
    head = Node(3)
    head.next = Node(12)
    head.next.next = Node(50)
    head.next.next.next = Node(28)
    print_list(head)
    head = delete(head)
    
    print_list(head)