class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."]*n for _ in range(n)]

        cols = set()
        positive_diags = set()
        negative_diags = set()

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in cols:
                    continue
                if row+col in positive_diags:
                    continue
                if row-col in negative_diags:
                    continue
                board[row][col] = "Q"
                cols.add(col)
                positive_diags.add(row+col)
                negative_diags.add(row-col)
                backtrack(row+1)
                board[row][col] = "."
                cols.remove(col)
                positive_diags.remove(row+col)
                negative_diags.remove(row-col)
        backtrack(0)
        return result
                
        