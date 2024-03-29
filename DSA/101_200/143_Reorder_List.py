# Definition for singly-linked list.
# Stack
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p1 = head
        stack = []

        while p1:
            stack.append(p1)
            p1 = p1.next
        
        counter = 1
        n = len(stack)

        while counter <= n:
            if counter % 2 == 1:
                curr = stack.pop()
                temp = head.next
                head.next = curr
            if counter % 2 == 0:
                head.next = temp
            
            head = head.next
            counter += 1
        
        head.next = None
        return head
