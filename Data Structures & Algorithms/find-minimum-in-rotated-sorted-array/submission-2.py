class Solution:
    def findMin(self, nums: List[int]) -> int:
        current = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > current:
                current = nums[i]
            else:
                return nums[i]
        
        return nums[0]