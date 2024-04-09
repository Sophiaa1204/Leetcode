# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.curr_sum = 0
        self.path = []
        self.res = False

    def traverse(self, node):
        if not node:
            return
        
        self.curr_sum += node.val
        if not node.left and not node.right:
            if self.curr_sum == self.targetSum:
                self.res = True
                # Can not return here!

        self.traverse(node.left)
        self.traverse(node.right)
        self.curr_sum -= node.val
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.targetSum = targetSum
        self.traverse(root)
        return self.res