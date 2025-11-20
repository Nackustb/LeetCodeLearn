from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n

        max_dp[0] = nums[0]
        min_dp[0] = nums[0]

        for i in range(1, n):
            x = nums[i]
            max_dp[i] = max(x, max_dp[i-1] * x, min_dp[i-1] * x)
            min_dp[i] = min(x, max_dp[i-1] * x, min_dp[i-1] * x)

        return max(max_dp)

# test
sol = Solution()
print(sol.maxProduct([2,3,-2,4]))  # Output: 6