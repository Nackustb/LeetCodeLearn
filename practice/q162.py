from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l , r = 0 ,len(nums) - 1 
        while l < r:
            m = l + (r-l) // 2
            if nums[m] > nums[m+1]:
                r = m 
            else:
                l = m + 1 
        
        return l

# Example usage:
solution = Solution()
nums = [1,2,1,3,5,6,4]
print(solution.findPeakElement(nums))  # Output: 5
