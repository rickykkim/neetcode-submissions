class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        best = -1
        
        while l < r:
            l_height = heights[l]
            r_height = heights[r]
            min_height = min(l_height, r_height)
            area = min_height * (r - l)

            if area > best:
                best = area

            if l_height < r_height:
                l += 1
            else:
                r -= 1
        
        return best