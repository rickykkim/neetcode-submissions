class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        
        top_list = sorted(counter.items(), key=lambda item: item[1])
        result = []
        rem = k
        for i in range(len(top_list)-1, -1, -1):
            result.append(top_list[i][0])
            rem -= 1
            if rem == 0:
                return result