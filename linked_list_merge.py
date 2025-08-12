'''
    Merge Two sorted linked lists
    
    Given the heads of 2 sorted linked lists: list1 & list2
    Merge the two lists into one sorted linked list and return the head of the new sorted linked list 
    
    List 1: 1 -> 2 -> 4
    List 2: 1 -> 3 -> 5
    
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 5
'''

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next 
        
def merge(list1, list2):
    temp_node = node = ListNode()
    
    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1 
            list1 = list1.next 
        else:
            node.next = list2
            list2 = list2.next 
        node = node.next 
        
    node.next = list1 if list1 else list2
    return temp_node.next 

def printList(node):
    while node is not None:
        print(node.val, end=" ")
        node = node.next
    print()
    
if __name__ == "__main__":
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    print("List1: ")
    printList(head1)
    
    head2 = ListNode(1)
    head2.next = ListNode(4)
    head2.next.next = ListNode(5)
    print("List2: ")
    printList(head2)
    
    res = merge(head1,head2)
    print("List 1 and 2 combined: ")
    printList(res)