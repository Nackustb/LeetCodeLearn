from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
    
        for ch in count_t:
            if count_t[ch] != count_s.get(ch, 0):
                return ch

# 测试
sol = Solution()
print(sol.findTheDifference("abcd", "abcde"))  # 输出: "e"
print(sol.findTheDifference("", "7"))          # 输出: "y"