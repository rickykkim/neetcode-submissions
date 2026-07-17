class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_nums = set(nums)
        begin = set()
        middle = set()
        end = set()

        for num in nums:
            if num - 1 in hash_nums and num + 1 in hash_nums:
                middle.add(num)
            elif num - 1 in hash_nums:
                end.add(num)
            else:
                begin.add(num)
        
        longest = 0
        for num in begin:
            length = 1
            next_num = num + 1
            while next_num in middle:
                length += 1
                next_num += 1
            
            if next_num in end:
                length += 1
            
            if length > longest:
                longest = length
        
        return longest