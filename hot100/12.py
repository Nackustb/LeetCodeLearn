from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = defaultdict(int)
        for x in t:
            cnt[x]+=1
        ch_type = len(cnt)

        ans_left, ans_right = -1, len(s)
        left = 0

        for right, x in enumerate(s):
            cnt[x] -= 1
            if cnt[x] == 0:
                ch_type -= 1
            while ch_type == 0:
                if right-left < ans_right-ans_left:
                    ans_left, ans_right = left, right
                cnt[s[left]] += 1
                if cnt[s[left]] > 0:
                    ch_type += 1
                left += 1

        return "" if ans_left<0 else s[ans_left: ans_right+1]

# Example usage:
sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
