from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n   # 每个数单独也能构成长度为1的LIS
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

# test
sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4