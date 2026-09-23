class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        for i in range(len(nums)):
            if i == 0:
                self.prefix.append(nums[i])
            else:
                self.prefix.append(nums[i] + self.prefix[-1])

    def sumRange(self, left: int, right: int) -> int:
        # [1 2 3 4]
        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)