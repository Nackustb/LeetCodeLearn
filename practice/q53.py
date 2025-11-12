from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide_and_conquer(left: int, right: int) -> int:
            # base case：只剩一个元素
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2

            # 分治：分别求左右区间的最大子数组和
            max_left_subarray = divide_and_conquer(left, mid)
            max_right_subarray = divide_and_conquer(mid + 1, right)

            # 计算跨越中点的最大子数组和
            max_left_border_sum = float('-inf')
            current_sum = 0
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                max_left_border_sum = max(max_left_border_sum, current_sum)

            max_right_border_sum = float('-inf')
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                max_right_border_sum = max(max_right_border_sum, current_sum)

            max_cross_subarray = max_left_border_sum + max_right_border_sum

            # 返回三者中的最大值
            return max(max_left_subarray, max_right_subarray, max_cross_subarray)

        return divide_and_conquer(0, len(nums) - 1)

# Example usage:
solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(nums))  # Output: 6