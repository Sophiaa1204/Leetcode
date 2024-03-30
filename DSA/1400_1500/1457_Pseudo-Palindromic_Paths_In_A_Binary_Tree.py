# Tree Traverse
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = 0
        self.record = [0] * 10
    
    def isValid(self):
        count = 0
        for i in self.record:
            if i % 2 != 0:
                count += 1
                if count > 1:
                    return False
        
        return True
    
    def traverse(self, node):
        if not node:
            return 
        
        self.record[node.val] += 1
        if not node.left and not node.right:
            if self.isValid():
                self.res += 1
        
        self.traverse(node.left)
        self.traverse(node.right)
        self.record[node.val] -= 1

    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res