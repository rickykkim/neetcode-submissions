class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Return 1-indexed indices / index1 < index2
        hash_map = {}
        
        for i in range(len(numbers)):
            rem = target - numbers[i]
            if numbers[i] in hash_map:
                return [hash_map[numbers[i]], i+1]
            else:
                hash_map[rem] = i+1