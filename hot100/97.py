from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=0
        count=0
        for x in nums:
            if count==0:
                res=x
            if x==res:
                count +=1
            else:
                count -=1
        return res

# test
s = Solution()
print(s.majorityElement([3,2,3]))  # Output: 3