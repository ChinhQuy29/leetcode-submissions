# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nums = []

        def bfs(node, height):
            if not node:
                return
            
            if height == len(nums):
                nums.append([node.val])
            elif height < len(nums):
                if height % 2 == 0:
                    nums[height].append(node.val)
                else:
                    nums[height].insert(0, node.val)
                    
            bfs(node.left, height + 1)
            bfs(node.right, height + 1)
    
        bfs(root, 0)
        return nums