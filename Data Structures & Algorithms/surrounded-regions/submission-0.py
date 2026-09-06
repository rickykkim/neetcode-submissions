class Solution:
    def solve(self, board: List[List[str]]) -> None:
        circles, queue = set(), deque()
        ROW, COL = len(board), len(board[0])
        for r in range(ROW):
            for c in range(COL):
                # Identify all circle locations
                if board[r][c] == "O":
                    circles.add((r, c))
                    # Identify all edge circles
                    if r == 0 or c == 0 or r == ROW - 1 or c == COL - 1:
                        queue.append((r, c))
        
        # Conduct BFS
        visited = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while queue:
            r, c = queue.popleft()
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= ROW or nc>= COL or (nr, nc) in visited or board[nr][nc] == "X":
                    continue
                queue.append((nr, nc))
        
        # Apply X to unvisited circles
        rem = circles - visited
        for r, c in rem:
            board[r][c] = "X"