class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_hash = set(nums)
        max_len = 0

        for n in nums:
            if n - 1 not in num_hash:
                length = 0
                curr = n
                while curr in num_hash:
                    length += 1
                    curr += 1
                max_len = max(max_len, length)
        
        return max_len