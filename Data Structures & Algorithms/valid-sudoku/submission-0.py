class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = set()
        col_check = {}
        square_check = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                # Exclude this case
                if board[i][j] == ".":
                    continue
                
                # Conduct row check
                if board[i][j] in row_check:
                    return False
                else:
                    row_check.add(board[i][j])
                
                key = str(int(i//3)) + str(int(j//3))

                if j not in col_check:
                    col_check[j] = []
                if key not in square_check:    
                    square_check[key] = []
                
                # Conduct col check
                col_check[j].append(board[i][j])
                if len(col_check[j]) > len(set(col_check[j])):
                    return False
                
                # Conduct square check
                square_check[key].append(board[i][j])
                if len(square_check[key]) > len(set(square_check[key])):
                    return False
            
            # Reset
            row_check = set()
        
        return True