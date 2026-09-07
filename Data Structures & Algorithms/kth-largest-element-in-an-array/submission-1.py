class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k

        def quick(l, r):
            p = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]
            if target == p:
                return nums[p]
            elif target < p:
                return quick(l, p-1)
            else:
                return quick(p+1, r)
        
        return quick(0, len(nums)-1)