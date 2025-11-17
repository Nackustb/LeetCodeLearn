class Solution:
    def subsets(self, nums):
        res = []
        path = []

        def backtrack(start):
            res.append(path[:])  
            for i in range(start, len(nums)):
                path.append(nums[i])      
                backtrack(i + 1)
                path.pop()                
                
        backtrack(0)
        return res
# test
s = Solution()
print(s.subsets([1,2,3]))  # [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]