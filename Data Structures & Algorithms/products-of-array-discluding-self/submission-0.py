class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = []
        
        acc = 1
        # Start from the left
        for i in range(n):
            if i == 0:
                product.append(acc)
            else:
                acc *= nums[i-1]
                product.append(acc)
        
        acc = 1
        # Start from the right
        for i in range(n-2, -1, -1):
            acc *= nums[i+1]
            product[i] *= acc 
        
        return product