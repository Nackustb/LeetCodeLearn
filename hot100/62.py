class Solution:
    def solveNQueens(self,n: int):
        res = [] 
        queens = [-1] * n

        def is_safe(row, col):
            for r in range(row):
                c = queens[r]
                if c == col or abs(row - r) == abs(col - c):
                    return False
            return True

        def backtrack(row):
            if row == n:
                board = []
                for r in range(n):
                    row_str = ['.'] * n
                    row_str[queens[r]] = 'Q'
                    board.append(''.join(row_str))
                res.append(board)
                return
            for col in range(n):
                if is_safe(row, col):
                    queens[row] = col
                    backtrack(row + 1)
                    queens[row] = -1

        backtrack(0)
        return res

# Example usage:
solution = Solution()
print(solution.solveNQueens(4))  # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]