from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # n = len(nums)
        # k %= n

        # def reverse(l, r):
        #     while l < r:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        #         r -= 1

        # reverse(0, n - 1)
        # reverse(0, k - 1)
        # reverse(k, n - 1)
        
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

# Example usage:
sol = Solution()
nums = [1,2,3,4,5,6,7]
sol.rotate(nums, 3)
print(nums)  # Output: [5,6,7,1,2,3,4]