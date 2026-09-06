class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cache = []
        visited = set()
        candidates.sort()

        def dfs(nums, curr, rem):
            tup = tuple(curr.copy())
            if tup in visited:
                return
            else:
                visited.add(tup)
            if rem == 0:
                cache.append(curr.copy())
                return
            elif rem < 0:
                return
            for j in range(len(nums)):
                dfs(nums[j+1:], curr + [nums[j]], rem - nums[j])
        
        for i in range(len(candidates)):
            dfs(candidates[i+1:], [candidates[i]], target - candidates[i])
        
        return cache