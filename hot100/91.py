class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n  
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]   

# test
s = Solution()
print(s.uniquePaths(3, 7))  # Output: 28