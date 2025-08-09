'''
    Linked List implementation
    
    Traversal within a linked list (singly)
'''

# Create a linked list node
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None    # None = NULL

def traverseList(head):
    while head is not None:  # Check for NULL ptr
        # Print current node
        print(head.data, end=' ')
        head = head.next  # Move to the next doe
    print()
        

def main():
    # The head and tail pointers should start at NULL initially.
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

        new_node = Node(num)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    print("\nLinked List contents:")
    traverseList(head)

if __name__ == "__main__":
    main()