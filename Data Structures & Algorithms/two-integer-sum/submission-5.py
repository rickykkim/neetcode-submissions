class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        
        l, r = 0, 1

        while True:
            total = nums[l] + nums[r]
            if total == target:
                return [l, r]
            elif r == len(nums) - 1:
                l += 1
                r = l + 1
            else:
                r += 1