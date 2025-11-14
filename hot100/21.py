from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row, col = rows - 1, 0  

        while row >= 0 and col < cols:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                row -= 1        
            else:
                col += 1        
                
        return False

# Example usage:
solution = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
print(solution.searchMatrix(matrix, target))  # Output: True