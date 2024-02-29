# Definition for singly-linked list.
# Two cases: odd number of nodes, even number of nodes
# Time Complexity: O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next # Go 1 step
            fast = fast.next.next # Go 2 steps
        
        return slow