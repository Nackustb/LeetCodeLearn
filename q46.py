from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        def backtrack(path,used):
            if len(path) == len(nums):
                result.append(path[:])
                return 
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()
                    used[i] = False
        
        backtrack([],used)
        return result


# Example usage:
solution = Solution()
nums = [1, 2, 3]
print(solution.permute(nums))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]