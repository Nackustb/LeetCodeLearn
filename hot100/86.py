from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict) 
        max_len = max(map(len, word_set))  
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for l in range(1, max_len + 1):
                if i - l < 0:
                    break
                if dp[i - l] and s[i - l:i] in word_set:
                    dp[i] = True
                    break   

        return dp[n]

# test  
sol = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))  # Output: True