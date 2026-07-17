class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            split = int((r - l) // 2) + l
            if nums[split] > nums[r]:
                l = split + 1
            else:
                r = split
        
        if target in nums[l:]:
            return nums[l:].index(target) + l
        elif target in nums[:l]:
            return nums[:l].index(target)
        else:
            return -1