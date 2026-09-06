class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 0:
            return []

        cache = []
        nums.sort()
        
        def dfs(i, curr, total):
            if total == target:
                cache.append(curr.copy())
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                curr.append(nums[j])
                dfs(j, curr, total + nums[j])
                curr.pop()
        
        dfs(0, [], 0)
        return cache