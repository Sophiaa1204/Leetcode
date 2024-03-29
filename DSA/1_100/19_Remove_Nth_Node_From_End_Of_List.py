# Definition for singly-linked list.
# Time Complexity: O(n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p1 = dummy
        dummy.next = head # take n steps
        
        for _ in range(n):
            p1 = p1.next

        p2 = dummy
        while p1.next:
            p1 = p1.next
            p2 = p2.next

        # get rid of nth node
        
        p2.next = p2.next.next

        return dummy.next