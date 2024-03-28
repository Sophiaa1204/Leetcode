# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.sum = 0
        self.path = ""

    def traverse(self, node):
        if not node:
            return
        
        self.path += str(node.val)
        if not node.left and not node.right:
            self.sum += int(self.path)
        
        self.traverse(node.left)
        self.traverse(node.right)

        self.path = self.path[:-1]

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.sum