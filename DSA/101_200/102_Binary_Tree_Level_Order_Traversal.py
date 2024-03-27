# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.traverse(root)
        return self.res

    def traverse(self, node):
        if not node:
            return
        
        # leaf node
        if not node.left and not node.right:
            self.path.append(str(node.val))
            self.res.append("->".join(self.path))
            self.path.pop()
            return 
        
        self.path.append(str(node.val))
        self.traverse(node.left)
        self.traverse(node.right)
        self.path.pop()
        