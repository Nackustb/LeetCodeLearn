from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        dp = [[0]*numRows for _ in range(numRows)]  
        res = []
        
        for i in range(numRows):
            dp[i][0] = 1
            dp[i][i] = 1
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            res.append(dp[i][:i+1])  
        
        return res

# test
sol = Solution()
print(sol.generate(5))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]