# Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.res = root.val

        def search(node):
            if not node:
                return
            if abs(node.val - target) < abs(self.res - target):
                self.res = node.val
            elif abs(node.val - target) == abs(self.res - target):
                self.res = min(self.res, node.val)
            
            if node.val > target:
                search(node.left)
            else:
                search(node.right)
            
        search(root)
        return self.res
