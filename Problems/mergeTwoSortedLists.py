"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.


"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode(0)
        while list1 and list2: 

            if list1.val < list2.val: 
                temp.next = list1 
                list1 = list1.next 
            else: 
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        temp.next = list1 or list2  
        return dummy.next 

def printList(head: Optional[ListNode]):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


printList(mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))))

            

        
