'''
    Linked List (singly) implementation for reversing the linked list.
    
    Initialize three pointers: prev = Null, curr = head, next = Null
    Iterate over the linked list and inside the loop:
        Store the next node, next = curt -> next
        Update the next ptr of curr to prev, curr -> next = prev
        Update the prev as curr and curr as next,  prev = curr, curr = next
        
    We need to use a "prev" pointer as a way to set head of the list as the tail 
    
    (Input) Head: 1 -> 2 -> 3 -> 4 -> NULL
    (Output) Head: 4 -> 3 -> 2 -> 1 -> NULL
    1 was originally the head, 4 was the tail.  We want 4 to be the head and 1 to the tail
'''
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

def reverse(head):
    # Initialize pointers
    curr = head 
    prev = None 
    
    # Traverse the linked list and update pointers
    while curr is not None:
        nextNode = curr.next    # Store the next pointer
        
        curr.next = prev        # Reverse the current node's 'next' pointer 
        
        prev = curr             # Move the pointers one position ahead.  
        curr = nextNode 
        
    return prev

def printList(node):
    while node is not None:
        print(f"{node.data}", end=" ")
        node = node.next
    print()
    

def main():
    head = None
    tail = None

    print("Enter values for the linked list. Press Q to quit.")

    while True:
        val = input("Enter a number (or Q to quit): ").strip()

        if val.lower() == 'q':
            break

        try:
            num = int(val)  # Convert input to integer
        except ValueError:
            print("Please enter a valid integer or Q to quit.")
            continue

        # Create a new node with the input value
        new_node = Node(num)

        # Filling up the linked list with values.
        # Case 1: Empty list head and tail point to the new node
        if head is None:
            head = new_node
            tail = new_node
        # Case 2: Append to existing list
        else:
            tail.next = new_node
            tail = new_node

    print("\nLinked List contents:")
    printList(head)
    
    # Reverse the list
    head = reverse(head)
    print("Linked list reversed:")
    printList(head)

if __name__ == "__main__":
    main()