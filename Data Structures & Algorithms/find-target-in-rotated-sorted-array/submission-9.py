class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] > nums[r]:
                if target <= nums[r] or target > nums[m]:
                    l = m + 1
                # if target < nums[m]:
                else:
                    r = m

            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                # if target > nums[m]:
                else:
                    l = m + 1

        return -1          