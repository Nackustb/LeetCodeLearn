from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):  
            farthest = max(farthest, i + nums[i])
            if i == end:
                jumps += 1
                end = farthest
                
        return jumps
# Example usage:
sol = Solution()
print(sol.jump([2,3,1,1,4]))  # Output: 2