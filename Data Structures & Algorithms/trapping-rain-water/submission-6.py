class Solution:
    def trap(self, height: List[int]) -> int:
        # trapped height is restricted to the shorter -> min(L, R)
        # at each point, (L, R) are different -> (max L, max R)
        # exclude 0 and len()-1
        # curr height >= min(max L, max R), we can't trap anything

        if len(height) < 3:
            return 0
        
        left, right = [0] * len(height), [0] * len(height)
        trap = 0

        # left
        best = -1
        for i in range(1, len(height)):
            if height[i-1] > best:
                best = height[i-1]
            left[i] = best
        
        # right
        best = -1
        for i in range(len(height)-2, -1, -1):
            if height[i+1] > best:
                best = height[i+1]
            right[i] = best
        
        # height
        for i in range(len(height)):
            min_height = min(left[i], right[i])
            if height[i] >= min_height:
                trap += 0
            else:
                trap += min_height - height[i]
        
        return trap