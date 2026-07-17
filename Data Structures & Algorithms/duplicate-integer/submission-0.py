class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_hash = dict()
        for num in nums:
            if num not in num_hash:
                num_hash[num] = 0
            num_hash[num] += 1

            if len(num_hash.keys()) < sum(num_hash.values()):
                return True
        
        return False