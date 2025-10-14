class Solution:
    def left(self,r, c, board):
        if not 0 <= r < len(board) or not 0 <= c < len(board):
            return True
        return board[r][c] != 'Q' and self.left(r-1,c-1, board)

    def right(self,r, c, board):
        if not 0 <= r < len(board) or not 0 <= c < len(board):
            return True
        return board[r][c] != 'Q' and self.right(r-1,c+1, board)

    def isSafe(self, r, c, board):
        for i in range(r):
            if board[i][c] == 'Q':
                return False
        return self.left(r,c, board) and self.right(r,c,board)

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for j in range(n)]
        result = []

        def dfs(n_queens, r):

            if n_queens == 0:
                oneBoard = []
                for row in board:
                    oneBoard.append("".join(row))
                result.append(oneBoard)
                return

            if r > n-1:
                return

            for c in range(n): # go thru each space of first row
                if board[r][c] == '.' and self.isSafe(r,c,board):
                    board[r][c] = 'Q' # choose
                    dfs(n_queens - 1, r+1)
                    board[r][c] = '.' # undo

        dfs(n, 0)

        return result