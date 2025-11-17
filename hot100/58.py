from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, path, target):
            if target == 0:
                res.append(path[:])  
                return
            if target < 0:
                return  
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, target - candidates[i])  
                path.pop()  
        
        backtrack(0, [], target)
        return res

# Example usage:
solution = Solution()
print(solution.combinationSum([2,3,6,7], 7))  # Output: [[7],[2,2,3]]
