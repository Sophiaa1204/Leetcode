# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Two Pointers & Dummy Node
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Pointer 1
        p1 = list1
        # Pointer 2
        p2 = list2
        # Dummy Node
        p = ListNode(-1)
        head = p

        while p1 and p2:
            if p1.val < p2.val:
                head.next = p1
                p1 = p1.next
            else:
                head.next = p2
                p2 = p2.next
            head = head.next
        
        if p1:
            head.next = p1
        if p2:
            head.next = p2
        
        return p.next