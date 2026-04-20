class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create a 9 x 9 board, create a 2nd helper function to see if it's a number. 
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] 
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[r //3, c //3]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r //3, c //3].add(board[r][c])
        
        return True