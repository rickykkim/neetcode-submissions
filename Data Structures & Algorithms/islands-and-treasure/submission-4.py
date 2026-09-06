class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        step = 1
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < ROW and 0 <= new_c < COL and grid[new_r][new_c] == INF:
                        grid[new_r][new_c] = step
                        queue.append((new_r, new_c))
            step += 1