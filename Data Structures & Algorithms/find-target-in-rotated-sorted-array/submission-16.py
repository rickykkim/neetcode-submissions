class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = int((l + r)//2)
            if nums[m] == target:
                return m
            
            # If the left side is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1