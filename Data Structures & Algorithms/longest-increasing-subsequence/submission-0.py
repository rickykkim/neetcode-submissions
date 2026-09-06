class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        cache = {}
        cache[nums[0]] = 1
        for i in range(1, len(nums)):
            max_val = -1
            for key, val in cache.items():
                if nums[i] > key:
                    max_val = max(max_val, val + 1)
            cache[nums[i]] = max(max_val, 1)
        
        return max(cache.values())
