from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = set(nums)
        cnt = 0
        for x in hash_map:
            if x-1 in hash_map:
                continue
            y = x+1
            while y in hash_map:
                y += 1
            cnt = max(cnt, y-x)
        return cnt
    
# test
s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))  # Output: 4
