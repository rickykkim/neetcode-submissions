class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # there is no point visiting a cell that's already 0
        # at the beginning of each DFS path, island += 1
        # update the grid as we go to prevent duplicate visits
        island = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    island += 1
                    dfs(r, c)
        return island