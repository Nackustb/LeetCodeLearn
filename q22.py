from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left: int, right: int, current: str):
            if left == right == n:
                result.append(current)
                return
            
            if left < n:
                backtrack(left + 1, right, current + '(')
            
            if right < left:
                backtrack(left, right + 1, current + ')')

        result = []
        backtrack(0, 0, "")
        return result

# Example usage:
solution = Solution()
n = 3
print(solution.generateParenthesis(n))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
