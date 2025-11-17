class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def backtrack(cur: str, left: int, right: int):
            if left == n and right == n:
                res.append(cur)
                return

            if left < n:
                backtrack(cur + '(', left + 1, right)

            if right < left:
                backtrack(cur + ')', left, right + 1)

        backtrack("", 0, 0)
        return res

# Example usage:
solution = Solution()
print(solution.generateParenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]