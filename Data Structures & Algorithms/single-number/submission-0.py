class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = set()
        cache_r = set()
        for num in nums:
            if num in cache:
                cache_r.add(num)
            else:
                cache.add(num)
        
        temp = cache - cache_r
        return list(temp)[0]