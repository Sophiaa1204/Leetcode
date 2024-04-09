# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        count = {}

        p = head
        while p:
            count[p.val] = count.get(p.val,0) + 1
            p = p.next
        
        dummy = ListNode(-1)
        p = head
        q = dummy
        # print(count)

        while p:
            if count[p.val] != 1:
                p = p.next
            else:
                temp = p.next
                p.next = None
                q.next = p
                q = q.next
                p = temp
        
        return dummy.next