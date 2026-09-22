class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 1 1 1
        # x 1 x x   x 1 2 x     x 1 2 8
        # 1 1 6 1   1 24 6 1    48 24 6 1
        left, right = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        for i in range(len(nums)-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        return res