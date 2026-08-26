# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nums = []
        
        def bfs(node, height):
            if not node:
                return 
            
            if height == len(nums):
                nums.append([node.val])
            else:
                nums[height].append(node.val)
            
            bfs(node.left, height + 1)
            bfs(node.right, height + 1)
        
        bfs(root, 0)
        
        res = []
        for level in nums:
            res.append(sum(level) / len(level))
        
        return res
        