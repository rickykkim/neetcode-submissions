class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        queue = deque()
        time, fresh = 0, 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if new_r < 0 or new_c < 0 or new_r >= ROW or new_c >= COL or grid[new_r][new_c] != 1:
                        continue
                    grid[new_r][new_c] = 2
                    queue.append((new_r, new_c))
                    fresh -= 1
            time += 1
        
        return -1 if fresh > 0 else time