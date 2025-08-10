'''
    Linked List (Singly) Full implementation
    
    Implements the following operations:
    1. Insertion
       -Insert at head
       -Insert at tail
       -Insert at a specific index
    2. Deletion
       -Delete at head
       -Delete at tail
       -Delete at a specific index
    3. Search for Element
       -Find a target value
       -Check if linked list is empty
    4. Length
       -Display current size of linked list
       -Check if linked list is empty
    5. Reversal
       -Reverse the linked list
       -Check if linked list is empty
    6. Display?

'''
# Linked List node 
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None        # next pointer set to NULL initially
        

def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")
    
    
def isEmpty():
    pass 

'''
    To insert an element into the linked list, the user has 3 options: 
    1. At the head
    2. At the tail
    3. At a specific index
'''
def insert_head(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_tail(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

def insert_at_index(head, data, index):
    """
    Insert at 0-based index.
    - index == 0: insert at head
    - 0 < index <= length: insert in middle or at tail
    - If index is out of bounds (> length), raise ValueError
    """
    if index < 0:
        raise ValueError("Index must be non-negative")

    if index == 0:
        return insert_head(head, data)

    # walk to node at position index-1
    curr = head
    pos = 0
    while curr is not None and pos < index - 1:
        curr = curr.next
        pos += 1

    if curr is None:
        # index > length
        raise ValueError("Index out of bounds")

    new_node = Node(data)
    new_node.next = curr.next
    curr.next = new_node
    return head
            

def main():
    # Initialize the head and tail pointers NULL.
    head = None
    tail = None
    print("Linked List implementation. ")

    while True:
        print("\nChoose an operation:")
        print("1. Insert a node")
        print("2. Delete a node")
        print("3. Search for a node")
        print("4. Get the size of the linked list")
        print("5. Reverse the linked list")
        print("6. Display linked list")
        print("Q. Quit")
        
        sel = input("Enter a number (or Q to quit): ").strip()
        if sel.lower() == 'q':
            print("\nQutting program!\n")
            break
        
        # Check user input.  Convert valid input to an int otherwise prompt the user to try again.
        try:
            num = int(sel)  # Convert input to integer
        except ValueError:
            print("Please enter a valid integer or Q to quit.")
            continue
        
        if sel == '1':
            print("\nWhere do you want to insert the value?")
            print("1. Insert at head")
            print("2. Insert at tail")
            print("3. Insert at specific index (0-based)")
            sub = input("Enter a sub-choice: ").strip()

            try:
                if sub == '1':
                    # value only
                    data = int(input("Enter value to insert: ").strip())
                    head = insert_head(head, data)

                elif sub == '2':
                    # value only
                    data = int(input("Enter value to insert: ").strip())
                    head = insert_tail(head, data)

                elif sub == '3':
                    # index first, then value
                    idx = int(input("Enter an index: ").strip())
                    data = int(input("Enter value to insert: ").strip())
                    head = insert_at_index(head, data, idx)

                else:
                    print("Invalid sub-choice.")
                    continue
                
                # optional: show list after each insert
                print("List after insert:")
                printList(head)

            except ValueError as e:
                print(f"Insert failed: {e}")
                
        elif sel == '2':
            print("\nNot Implemented yet")
        elif sel == '3':
            print("\nNot Implemented yet")
        elif sel == '4':
            print("\nNot Implemented yet")
        elif sel == '5':
            print("\nNot Implemented yet")
        elif sel == '6':
            print()
            printList(head)           
           
if __name__ == "__main__":
    main()