class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [[nums[0]]]
        
        res = []
        def dfs(node, curr):
            temp = curr + [node]
            if len(temp) == len(nums):
                res.append(temp)
                return
            else:
                rem = set(nums) - set(temp)
            
            for num in rem:
                dfs(num, temp)
            return

        for num in nums:
            dfs(num, [])
        
        return res