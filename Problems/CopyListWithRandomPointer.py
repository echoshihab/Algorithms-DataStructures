"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


#O(n) time complexity
def copyRandomList(head: Optional[Node]) -> Optional[Node]:

        oldToNewDict = {None: None}

        # create hashmap with copy of unlinked node of original as value
        curr = head
        while curr:             
             oldToNewDict[curr] = Node(curr.val)
             curr = curr.next

        # create the links for next and random as before using the hashmap
        curr = head
        while curr:            
            oldToNewDict[curr].next = oldToNewDict.get(curr.next)  # will be none if value is None
            oldToNewDict[curr].random = oldToNewDict.get(curr.random) # will be none if value is None
            curr = curr.next

        return oldToNewDict[head]  # if no head, the result will will be None due to the dict initialization with None key

        



