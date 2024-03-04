# BFS
# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.append(root)
        
        step = 0

        while q:
            step += 1
            size = len(q)

            for i in range(size):
                cur = q.popleft()
                if not cur.left and not cur.right:
                    return step
                if cur.left:
                    q.append(cur.left) 
                if cur.right:
                    q.append(cur.right)
        
        return -1