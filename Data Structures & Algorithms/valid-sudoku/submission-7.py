class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ro = defaultdict(set)
        co = defaultdict(set)
        squ = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in ro[r] 
                    or board[r][c] in co[c]
                    or board[r][c] in squ[( r // 3, c // 3)]):
                    return False
                ro[r].add(board[r][c])
                co[c].add(board[r][c])
                squ[( r // 3, c // 3)].add(board[r][c])
        
        return True