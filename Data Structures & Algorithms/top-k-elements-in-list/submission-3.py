class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keys = dict()
        for num in nums:
            if num not in keys:
                keys[num] = 0
            keys[num] += 1
        
        output = []
        count = 0
        top_list = sorted(keys.items(), key=lambda item: item[1], reverse=True)
        for key, val in top_list:
            output.append(key)
            count += 1
            if count == k:
                break
        
        return output