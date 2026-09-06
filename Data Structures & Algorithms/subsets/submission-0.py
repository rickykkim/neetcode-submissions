class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        cache = []
        def dfs(curr, rem):
            if len(rem) == 0:
                cache.append(curr)
                return
            dfs(curr.copy(), rem[1:])
            dfs(curr.copy() + [rem[0]], rem[1:])
        
        dfs([], nums[1:])
        dfs([nums[0]], nums[1:])

        return cache