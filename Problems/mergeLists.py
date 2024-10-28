from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head: Optional[ListNode]):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


"""Given two lists, merge so that the lists are merged with alternating nodes
e.g. 1 => 2 => 3 => 4  and 8 => 7 => 6 => 5 becomes

1 => 8 => 2 => 7 => 3 => 6 => 4 => 5

assume that the second list is always shorter or equal to the first list

"""


def mergeListAlternate(list1: Optional[ListNode], list2: Optional[ListNode]):
    head = list1
    while list2:
        tmp1, tmp2 = list1.next, list2.next
        list2.next = list1.next
        list1.next = list2
        list1 = tmp1
        list2 = tmp2 
    
    printList(head)

list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(8, ListNode(7, ListNode(6)))
                                                        
                                                                    
mergeListAlternate(list1, list2)

    