class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, curr):
            total = sum(curr)
            if total == target:
                res.append(curr)
                return
            if i >= len(nums) or total > target:
                return
            
            dfs(i, curr + [nums[i]])
            dfs(i+1, curr)

        dfs(0, [])
        return res