class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1
        tupMap = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        
        res = []
        for i, (key, val) in enumerate(tupMap):
            if i == k:
                break
            res.append(key)
        return res