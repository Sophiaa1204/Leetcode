# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def traverse(node,currDep,depth,val):
            if not node:
                return
            if currDep == depth - 1:
                temp_left = node.left
                temp_right = node.right
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                node.left.left = temp_left
                node.right.right = temp_right
                return
            
            traverse(node.left,currDep+1,depth,val)
            traverse(node.right,currDep+1,depth,val)

        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            traverse(root,1,depth,val)
            return root