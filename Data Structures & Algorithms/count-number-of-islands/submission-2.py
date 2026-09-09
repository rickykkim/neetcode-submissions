class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # start from everywhere
        # update grid to 0 when visited
        # DFS
        # when blocked, add count value

        # total number of islands
        island = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return 0
            
            # discovered "1"
            grid[r][c] = "0"
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        # start from every coordinate
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if dfs(r, c) > 0:
                    island += 1
        
        return island