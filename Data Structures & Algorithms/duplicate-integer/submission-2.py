class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        
        key = set()
        for num in nums:
            if num not in key:
                key.add(num)
            else:
                return True
        
        return False