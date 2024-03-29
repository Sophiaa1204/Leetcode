# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def findMax(root):
            if not root:
                return 0,None # max_length, last_number
            
            left_max, left_num = findMax(root.left)
            right_max, right_num = findMax(root.right)
            # print(left_max,left_num,right_max,right_num,root.val)

            curr_max = -1
            curr_val = root.val

            if left_num == root.val + 1:
                curr_max = max(curr_max, left_max+1)
                self.res = max(self.res,curr_max)
            if right_num == root.val + 1:
                curr_max = max(curr_max, right_max+1)
                self.res = max(self.res,curr_max)
            if curr_max == -1:
                curr_max = 1
                self.res = max(self.res,curr_max)