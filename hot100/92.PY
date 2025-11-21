class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(m):
            dp[0] += grid[i][0]    # 第一列只能从上往下累加
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]

# test
s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(s.minPathSum(grid))  # Output: 7