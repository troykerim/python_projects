class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 
        
def insert_front(head, data):
    # Create a new node
    new_node = Node(data)
    new_node.next = head  
    
    if head is not None:
        head.prev = new_node
    return new_node

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
    head = insert_front(head, data)
    
    printList(head)