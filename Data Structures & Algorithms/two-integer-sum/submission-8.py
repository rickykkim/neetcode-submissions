class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx in range(len(nums)):
            # what someone needs: someone's idx
            if nums[idx] in cache:
                temp = [idx, cache[nums[idx]]]
                return sorted(temp)
            cache[target - nums[idx]] = idx
        