class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        
        top_list = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        result = []
        rem = k
        for top in top_list:
            result.append(top[0])
            rem -= 1
            if rem == 0:
                return result