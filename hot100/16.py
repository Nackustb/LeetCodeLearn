from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        
        suf = 1
        for j in range(n-1, -1, -1):
            pre[j] *= suf
            suf *= nums[j]
        
        return pre

# Example usage:
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))  # Output: [24,12,8,6]