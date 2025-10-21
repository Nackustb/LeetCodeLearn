class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}  
        cnt = sum(1 for c in s[:k] if c in vowels)
        res = cnt

        for j in range(k, len(s)):
            if s[j - k] in vowels:
                cnt -= 1
            if s[j] in vowels:
                cnt += 1
            res = max(res, cnt)

        return res

# Example usage:
solution = Solution()
s = "abciiidef"
k = 3
print(solution.maxVowels(s, k))  # Output: 3