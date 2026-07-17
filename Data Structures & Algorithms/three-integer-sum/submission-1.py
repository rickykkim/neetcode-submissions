class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n-2):
            first = nums[i]
            l = i + 1
            r = n - 1

            while l < r:
                second = nums[l]
                third = nums[r]
                total = first + second + third

                if total == 0:
                    triplet = sorted([first, second, third])
                    if triplet not in result:
                        result.append(triplet)
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        
        return result