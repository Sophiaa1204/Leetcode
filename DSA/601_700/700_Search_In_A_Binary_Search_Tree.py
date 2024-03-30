# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def search(self, node, val):
        if not node:
            return None
        if node.val == val:
            return node
        
        left = self.search(node.left,val)
        right = self.search(node.right,val)

        return left if left else right
      
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search(root,val)