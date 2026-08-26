# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(p, q):
            if not q and not p:
                return True
            
            if not p:
                return False
            
            if not q:
                return False
            
            return (p.val == q.val) and isSym(p.left, q.right) and isSym(p.right, q.left)
        
        if not root:
            return True

        return isSym(root.left, root.right)