class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        cache = [0] * n
        cache[0] = 1
        cache[1] = 2

        for i in range(2, n):
            cache[i] = cache[i-2] + cache[i-1]

        return cache[-1]