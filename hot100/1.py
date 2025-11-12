from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for index,num in enumerate(nums):
            if target - num in hashset:
                return [hashset[target - num], index]
            hashset[num] = index
        return []
# Example usage:
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))  # Output: [0, 1]