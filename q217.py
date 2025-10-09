from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num not in hash_set:
                hash_set.add(num)
            else:
                return True
        return False
# test
s = Solution()
print(s.containsDuplicate([1,2,3,1]))  # True
print(s.containsDuplicate([1,2,3,4]))  # False