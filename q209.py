from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        total = 0
        left = 0

        for right in range(n):
            total += nums[right]
            # 尽可能收缩左边界
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if res == n + 1 else res
    
# Example usage:
solution = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(solution.minSubArrayLen(target, nums))  # Output: 2