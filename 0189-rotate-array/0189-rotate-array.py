class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        k = k % len(nums)
        first = nums[:len(nums) - k]
        second = nums[len(nums) - k:]
        nums[:] = second + first

        
        