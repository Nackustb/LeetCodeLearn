from typing import List
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         i = 0
#         while i < len(nums):
#             if nums[i] == 0:
#                 # 所有元素前移一位
#                 for j in range(i, len(nums) - 1):
#                     nums[j] = nums[j + 1]
#                 # 最后一个位置补 0
#                 nums[-1] = 0
#             else:
#                 i += 1  # 只有当当前不是 0 时才移动 i

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0  # 指向下一个非零应放的位置
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

# 测试
if __name__ == "__main__":
    s = Solution()
    arr = [1,1,0,3,12]
    s.moveZeroes(arr)
    print(arr)  # ✅ 输出: [1,3,12,0,0]