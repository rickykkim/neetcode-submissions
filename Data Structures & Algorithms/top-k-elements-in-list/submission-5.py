class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        for num in nums:
            if num not in cache:
                cache[num] = 0
            cache[num] += 1
        
        cache_tuple = []
        for key, value in cache.items():
            cache_tuple.append((-value, key))
        
        result = []
        heapq.heapify(cache_tuple)
        while len(result) < k:
            value, key = heapq.heappop(cache_tuple)
            result.append(key)
        return result