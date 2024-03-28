# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.maxD = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findMax(root)
        return self.maxD

    def findMax(self, node):
        if not node:
            return 0

        left_max = self.findMax(node.left)
        right_max = self.findMax(node.right)

        self.maxD = max(self.maxD, left_max+right_max)

        return max(left_max,right_max) + 1