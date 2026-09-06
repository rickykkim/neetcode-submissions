class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            max_val = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    max_val = max(max_val, dp[j])
            dp[i] = 1 + max_val
        
        return max(dp)