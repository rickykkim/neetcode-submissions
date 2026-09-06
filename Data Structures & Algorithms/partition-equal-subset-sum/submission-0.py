class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        cache = set()
        target = sum(nums) // 2
        cache.add(0)
        for i in range(len(nums)):
            next_cache = cache.copy()
            for val in cache:
                next_cache.add(val + nums[i])
            cache = next_cache
        
        return target in cache