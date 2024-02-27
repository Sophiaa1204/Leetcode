# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Decompose the problem
        def traverse(node):
            # Base Case
            if not node:
                return None
            
            inverted_left = traverse(node.left)
            inverted_right = traverse(node.right)

            node.right = inverted_left
            node.left = inverted_right
            
            # Return should be in the same type
            return node 
        
        traverse(root)
        return root