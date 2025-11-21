class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2
        
        # Step 1: 找 pivot
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Step 2: 找右边第一个比 pivot 大的
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: 反转右区间
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
# test
s = Solution()
nums = [1,2,3]
s.nextPermutation(nums)
print(nums)  # Output: [1,3,2]