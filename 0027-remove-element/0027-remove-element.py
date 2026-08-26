class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums) - 1
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                count += 1
                continue

            while end >= 0 and nums[end] == val:
                end -= 1
            
            if i < end:
                nums[i] = nums[end]
                nums[end] = val
                count += 1
            else:
                break 

        return count