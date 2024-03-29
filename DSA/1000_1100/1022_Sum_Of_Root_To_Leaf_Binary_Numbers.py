# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.path = []
        self.res = None

        def traverse(node):
            if not node:
                return 

            self.path.append(chr(ord('a') + node.val))
            if not node.left and not node.right:
                curr = "".join(self.path[::-1])
                if self.res == None or curr < self.res:
                    self.res = curr
            
            traverse(node.left)
            traverse(node.right)
            self.path.pop()

        traverse(root)
        return self.res