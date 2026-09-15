class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # start at every position possible
        # if we encounter 0, stop there and update island if count > 0
        # as we traverse through the grid, update any 1s to 0s

        island = 0

        def dfs(r, c):
            nonlocal island
            # terminating conditions
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return
            
            # indicate that we visited this cell
            grid[r][c] = "0"
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
            return
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    island += 1
                    dfs(r, c)
        
        return island