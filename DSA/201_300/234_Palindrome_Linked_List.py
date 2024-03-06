# Definition for singly-linked list.

# Time Complexity: O(n)
# Space Complexity: O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        num_list = []

        while head:
            num_list.append(head.val)
            head = head.next
        
        left = 0
        right = len(num_list) - 1

        while left < right:
            if num_list[left] != num_list[right]:
                return False
            left += 1
            right -= 1
        
        return True
        