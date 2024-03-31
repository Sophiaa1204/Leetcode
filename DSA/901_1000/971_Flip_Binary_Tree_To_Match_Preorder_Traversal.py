# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.idx = 0
        self.voyage = []
        self.res = []
        self.canFlip = True
    
    def traverse(self,node):
        if not node or not self.canFlip:
            return
        if node.val != self.voyage[self.idx]:
            self.canFlip = False
            return
        
        self.idx += 1
        if node.left and node.left.val != self.voyage[self.idx]:
            temp = node.left
            node.left = node.right
            node.right = temp
            self.res.append(node.val)
        
        self.traverse(node.left)
        self.traverse(node.right)

    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.voyage = voyage
        self.traverse(root)

        if self.canFlip:
            return self.res
        else:
            return [-1]