class Solution:
    def sortColors(self, nums):
        p0, p2 = 0, len(nums) - 1
        i = 0

        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:  # nums[i] == 1
                i += 1

# test
s = Solution()
nums = [2,0,2,1,1,0]
s.sortColors(nums)
print(nums)  # Output: [0,0,1,1,2,2]