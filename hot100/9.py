from collections import defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1
        if s_count == p_count:
            res.append(0)
        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            if s_count == p_count:
                res.append(i + 1)
        return res

# Example usage:
sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))  # Output: [0, 6]
