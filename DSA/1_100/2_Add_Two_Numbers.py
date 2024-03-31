# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        head = dummy
        p1 = l1
        p2 = l2
        add = 0

        while p1 and p2:
            curr = p1.val + p2.val + add
            add = 0
            if curr >= 10:
                head.next = ListNode(curr % 10)
                add += 1
            else:
                head.next = ListNode(curr)
            head = head.next
            p1 = p1.next
            p2 = p2.next
        
        while p1:
            curr = p1.val + add
            add = 0
            if curr >= 10:
                head.next = ListNode(curr % 10)
                add = 1
            else:
                head.next = ListNode(curr)
            head = head.next
            p1 = p1.next
        
        while p2:
            curr = p2.val + add
            add = 0
            if curr >= 10:
                head.next = ListNode(curr % 10)
                add = 1
            else:
                head.next = ListNode(curr)
            head = head.next
            p2 = p2.next
        
        if add == 1:
            head.next = ListNode(1)
        
        return dummy.next