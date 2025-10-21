class Solution:
    def fib(self, n: int) -> int:
        if n < 2 :
            return n 
        else:
            return self.fib(n-1) + self.fib(n-2)
# Example usage:
solution = Solution()
n = 5
print(solution.fib(n))  # Output: 5