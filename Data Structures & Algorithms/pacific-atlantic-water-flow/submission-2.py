class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 1) pacific cells -> equal/higher cells -> collect all endpoints
        # 2) atlantic cells -> do the same
        # DFS

        pac, atl = set(), set()

        def dfs(r, c, visit):
            visit.add((r, c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if new_r < 0 or new_c < 0 or new_r >= len(heights) or new_c >= len(heights[0]) or heights[new_r][new_c] < heights[r][c] or (new_r, new_c) in visit:
                    continue
                dfs(new_r, new_c, visit)
        
        for c in range(len(heights[0])):
            # pacific
            dfs(0, c, pac)
            # atlantic
            dfs(len(heights) - 1, c, atl)
        
        for r in range(len(heights)):
            # pacific
            dfs(r, 0, pac)
            # atlantic
            dfs(r, len(heights[0])-1, atl)
        
        # take the overlap of pacific and atlantic -> return
        new_pac = pac - (pac - atl)
        return [list(p) for p in new_pac]

