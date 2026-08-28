# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def bfs(node, height):
            if not node:
                return 
            
            if height == len(res):
                res.append(node.val)

            bfs(node.right, height + 1)
            bfs(node.left, height + 1)
        
        bfs(root, 0)
        return res