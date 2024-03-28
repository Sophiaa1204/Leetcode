# Definition for a binary tree node.
# Traverse
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = 0
        self.depth = 0
    
    def traverse(self, node):
        if not node:
            return 
        
        self.depth += 1
        # No leaf node
        if not node.left and not node.right:
            if self.depth > self.res:
                self.res = self.depth
        
        self.traverse(node.left)
        self.traverse(node.right)
        self.depth -= 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res