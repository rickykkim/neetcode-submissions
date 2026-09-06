class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val, max_val = 1, 1
        res = nums[0]
        for num in nums:
            temp = num * max_val
            max_val = max(num, temp, num*min_val)
            min_val = min(num, temp, num*min_val)
            res = max(res, max_val, min_val)
        return res