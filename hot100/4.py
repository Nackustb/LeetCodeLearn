from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right, num in enumerate(nums):
            if num != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
# test
s = Solution()
print(s.moveZeroes([0,1,0,3,12]))  # Output: [1,3,12,0,0]