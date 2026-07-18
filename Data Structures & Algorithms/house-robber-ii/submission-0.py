class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        cache = []
        for _ in range(len(nums)):
            cache.append([-1, -1])

        def dfs(i, flag):
            if i >= len(nums):
                return 0
            
            if cache[i][flag] != -1:
                return cache[i][flag]
            
            if i == len(nums) - 1:
                if flag:
                    cache[i][flag] = 0
                    return 0
                else:
                    cache[i][flag] = nums[i]
                    return nums[i]
            
            cache[i][flag] = max(nums[i] + dfs(i+2, flag), dfs(i+1, flag))
            return cache[i][flag]
        
        return max(dfs(0, True), dfs(1, False))