class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        val = nums[k]
        for i in range(len(nums)):
            if nums[i] != nums[k]:
                nums[k + 1] = nums[i]
                k += 1

        return k + 1