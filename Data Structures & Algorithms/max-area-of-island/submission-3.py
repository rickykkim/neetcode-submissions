class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # every time we find an island, we update it by doing max()
        # go through every island search through DFS
        # initiate DFS when a cell is 1
        # as we go through different DFS paths, we would update visited 1 -> 0
        max_area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area