class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        
        def dfs(r, c, count):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return count
            if grid[r][c] == "0":
                return count
            else:
                grid[r][c] = "0"

            return dfs(r+1, c, count+1) + dfs(r-1, c, count+1) + dfs(r, c+1, count+1) + dfs(r, c-1, count+1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if dfs(r, c, 0) > 0:
                    islands += 1
        return islands