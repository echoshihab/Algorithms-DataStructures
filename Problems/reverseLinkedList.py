"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # need to keep track of the next node
    # need to keep track of prev node

    prev_node = None

    while head and head.next:
        temp_node = head.next  
        head.next = prev_node 
        prev_node = head  
        head = temp_node 
        if head.next == None:
            head.next = prev_node
            break

    return head
    

result = reverseList(ListNode(1, ListNode(2, ListNode(3))))


def printList(head: Optional[ListNode]):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

printList(result)



def reverseList2(head: ListNode) -> ListNode:
    prev_node = None

    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node

    return prev_node

result = reverseList2(ListNode(1, ListNode(2, ListNode(3))))

printList(result)