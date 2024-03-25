# Definition for singly-linked list.
# Time Complexity: O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1) # Less than x
        dummy2 = ListNode(-2) # Larger than x
        p1 = dummy1 # pointer 1
        p2 = dummy2 # pointer 2
        p = head

        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            temp = p.next
            p.next = None
            p = temp
        
        p1.next = dummy2.next
        return dummy1.next
