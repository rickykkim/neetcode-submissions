class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit):
            visit.add((r, c))
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS
                        and (nr, nc) not in visit
                        and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visit)

        for c in range(COLS):
            dfs(0, c, pac)              # top edge → Pacific
            dfs(ROWS - 1, c, atl)       # bottom edge → Atlantic
        for r in range(ROWS):
            dfs(r, 0, pac)              # left edge → Pacific
            dfs(r, COLS - 1, atl)       # right edge → Atlantic

        return [list(cell) for cell in pac & atl]