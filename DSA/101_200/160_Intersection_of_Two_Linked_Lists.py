# Definition for singly-linked list.
# Two pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB

        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
        
        return p1