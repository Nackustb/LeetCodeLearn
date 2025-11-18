from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int, path: List[str]):
            if start == len(s):  # 字符串被分割完
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                substring = s[start:end+1]
                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(end + 1, path)
                    path.pop()  # 回溯

        backtrack(0, [])
        return res

# Example usage:
solution = Solution()
print(solution.partition("aab"))  # Output: [["a","a","b"],["aa"]]