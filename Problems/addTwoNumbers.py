"""You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n+m)
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
    l1Text = ''

    while l1:
        l1Text = f"{l1.val}{l1Text}"
        l1 = l1.next


    l2Text = ''
    while l2:
        l2Text = f"{l2.val}{l2Text}"
        l2 = l2.next
    

    total = str(int(l1Text) + int(l2Text))

    result_stack = []
    #convert total to text, use a stack and then write to listnode

    for char in total:
        result_stack.append(int(char))

    head = curr = ListNode()
    while len(result_stack):
        curr.next = ListNode(result_stack.pop())
        curr = curr.next
    

    return head.next
