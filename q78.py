from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []    
        subset = []     

        def backtrack(start: int):
            result.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])       
                backtrack(i + 1)             
                subset.pop()                 

        backtrack(0)
        return result


# Example usage:
solution = Solution()
nums = [1, 2, 3]
print(solution.subsets(nums))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]