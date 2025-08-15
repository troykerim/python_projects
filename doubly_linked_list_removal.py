'''
    Doubly Linked List
    
    Remove a node at the head of the Linked List
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Function to delete the first node (head) of the list and return the second node as the new head
def del_head(head):
  
    # Check if the list is empty
    if head is None:
        return None

    # Store in temp for deletion later
    temp = head

    # Move head to the next node
    head = head.next

    # Set prev of the new head
    if head is not None:
        head.prev = None

    # Return new head
    return head

def del_last(head):
  
    # Edge cases
    if head is None:
        return None
    if head.next is None:
        return None

    # Traverse to the last node
    curr = head
    while curr.next is not None:
        curr = curr.next

    # Update the previous node's next pointer
    if curr.prev is not None:
        curr.prev.next = None

    # Return the updated head
    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()
    

if __name__ == "__main__":
  
    # 1 <-> 2 <-> 3 <-> 4
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    
    head.next.next = Node(3)
    head.next.next.prev = head.next
    
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    print("Original Linked List: ", end="")
    print_list(head)

    print("Deletion of the head: ", end="")
    head = del_head(head)
    print_list(head)
    
    print("Deletion at the end: ", end="")
    head = del_last(head)
    print_list(head)
    