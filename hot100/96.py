class Solution:
    def singleNumber(self, nums):
        res = 0
        for x in nums:
            res ^= x
        return res


# test
s = Solution()
print(s.singleNumber([4,1,2,1,2]))  # Output: 4