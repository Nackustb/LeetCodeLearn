from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        count = {0: 1}  
        res = 0
        for num in nums:
            pre += num
            if pre - k in count:
                res += count[pre - k]
            count[pre] = count.get(pre, 0) + 1
        return res

# Example usage:
sol = Solution()
print(sol.subarraySum([1,1,1], 2))  # Output: 2