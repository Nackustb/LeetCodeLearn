from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start: int):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)        
                backtrack(i + 1)     
                path.pop()              

        backtrack(1)
        return result

# Example usage:
solution = Solution()
n = 4
k = 2
print(solution.combine(n, k))  # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]