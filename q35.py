from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l , r = 0 ,len(nums)-1
        while l <= r :
            m = l + (r-l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1 
            else:
                r = m - 1 
        return l 
            
# Example usage:
solution = Solution()
nums = [1,3,5,6]
target = 5
print(solution.searchInsert(nums, target))  # Output: 2