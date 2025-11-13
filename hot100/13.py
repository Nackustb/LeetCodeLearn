from typing import List
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = nums[0]
#         current_sum = 0
#         for num in nums:
#             if current_sum < 0:
#                 current_sum = 0
#             current_sum += num
#             max_sum = max(max_sum, current_sum)
#         return max_sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            left_max = helper(left, mid)
            right_max = helper(mid + 1, right)

            left_border_sum = float('-inf')
            current_sum = 0
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                left_border_sum = max(left_border_sum, current_sum)

            right_border_sum = float('-inf')
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_border_sum = max(right_border_sum, current_sum)

            cross_sum = left_border_sum + right_border_sum

            return max(left_max, right_max, cross_sum)

        return helper(0, len(nums) - 1)




# Example usage:
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
