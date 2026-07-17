class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = [False]

        def dfs(r, c, i):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            if board[r][c] != word[i]:
                return
            
            if board[r][c] == word[i] and i == len(word) - 1:
                res[0] = True
                return
            elif i == len(word) - 1:
                return
            
            original = board[r][c]
            board[r][c] = "#"
            dfs(r+1, c, i+1)
            dfs(r-1, c, i+1)
            dfs(r, c+1, i+1)
            dfs(r, c-1, i+1)
            board[r][c] = original
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, 0)
        
        return res[0]