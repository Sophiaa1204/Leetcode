# Definition for a binary tree node.
# Decompose the question
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(nodeP,nodeQ):
            if not nodeP and not nodeQ:
                return True
            if not nodeP and nodeQ:
                return False
            if not nodeQ and nodeP:
                return False
            
            left_same = traverse(nodeP.left,nodeQ.left)
            right_same = traverse(nodeP.right,nodeQ.right)

            return nodeP.val == nodeQ.val and left_same and right_same
        
        return traverse(p,q)