"""Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    arr = [0] * 30
    pointer = 0
    while head:
        arr[pointer] = head
        head = head.next
        pointer += 1
    
    lenArr = pointer
    removeIndex = lenArr - n

    if removeIndex == 0:
        return None if arr[1] == 0 else arr[1]
        

    prevNode = arr[removeIndex - 1]
    nextNode = None


    if removeIndex + 1 >= lenArr:
        prevNode.next = nextNode
        return arr[0]
    else:
        nextNode = arr[removeIndex + 1]

    prevNode.next = nextNode
    return arr[0]


    
def removeNthFromEnd2(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # set dummy node

    first = dummy = ListNode()

    second = dummy.next = head

    # set first and second marker
    while n > 0:
        second = second.next
        n -= 1
    
    # loop till the markers are set appropriately
    while second:
        first = first.next
        second = second.next

    #delete the node
    first.next = first.next.next


    return dummy.next