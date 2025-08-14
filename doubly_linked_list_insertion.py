class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 
        
def insert_head(head, data):
    # Create a new node
    new_node = Node(data)
    new_node.next = head  
    
    if head is not None:
        head.prev = new_node
    return new_node

def insert_tail(head, data):
    new_node = Node(data)
    
    if head is None:
        head = new_node
    else:
        curr = head 
        # Iterate over the entire linked list until you reach null
        while curr.next is not None:
            curr = curr.next  # Move the current pointer to the next node for each iteration.
        # At the end of the while loop, set the previous tail element's next pointer to point to the new node
        curr.next = new_node
        new_node.prev = curr    # Set the new tail node to point back to the previous node.
    return head 


    # This function can be used to replace the two functions above
def insert_any_index(head, data, pos):
    new_node = Node(data)
    
    # Inserting at the beginning
    if pos == 1:
        new_node.next = head
        
        # Check is the linked list is empty, set previous pointer to the new node
        if head is not None:
            head.prev = new_node
        
        # Set the new node as the new head of the linked list
        head = new_node
        return head 

    curr = head 
    for _ in range(1, pos - 1):
        if curr is None:
            print("Position is out of bounds.")  # Edge case if they ask for an index not in the linked list 
            return head 
        curr = curr.next 
    
    if curr is None:
        print("Position is out of bounds.")  # Edge case if they ask for an index not in the linked list 
        return head 
        
    new_node.prev = curr 
    new_node.next = curr.next 
    curr.next = new_node
    
    # If the new node is not the last node, update the prev pointer of the next node to point to the new node
    if new_node.next is not None:
        new_node.next.prev = new_node 
    return head 

 
def printList(head):
    curr = head 
    while curr is not None:
        print(f"{curr.data}", end=' ')
        curr = curr.next 
    print()
    
if __name__ == "__main__":
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next= Node(5)
    
    print("Original Linked List: ", end=' ')
    printList(head)
    
    print("After inserting a Node in the front: ", end=' ')
    data = 1 
    head = insert_head(head, data)
    
    printList(head)
    
    
    data = 55
    print("Inserting a Node at the end: ", end=" ")
    head = insert_tail(head,data)
    printList(head)
    
    