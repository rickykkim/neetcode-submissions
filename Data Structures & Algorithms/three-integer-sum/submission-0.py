class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        result = []

        for i in range(n-2):
            first = sorted_nums[i]
            l = i + 1
            r = n - 1

            while l < r:
                second = sorted_nums[l]
                third = sorted_nums[r]
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