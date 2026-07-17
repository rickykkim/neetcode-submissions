class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:                # target?
                return m

            if nums[l] <= nums[m]:               # left sorted half?
                if nums[l] <= target <= nums[m]: # within range?
                    r = m - 1                    # eliminate right half
                else:
                    l = m + 1
            else: #(nums[m] < nums[r])           right sorted half?
                if nums[m] <= target <= nums[r]: # within range?
                    l = m + 1                    # eleminate left half
                else:
                    r = m - 1
        return -1