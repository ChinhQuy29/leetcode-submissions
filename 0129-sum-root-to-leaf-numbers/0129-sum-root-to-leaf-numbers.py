# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        
        def getNums(root, val):
            if not root:
                return

            if not root.left and not root.right:
                nums.append(val * 10 + root.val)
                return
            
            getNums(root.left, val * 10 + root.val)
            getNums(root.right, val * 10 + root.val)

        if not root:
            return 0

        getNums(root, 0)
        return sum(nums)