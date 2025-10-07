# from typing import List
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         result = 0
#         for i in range(len(nums)):
#             if nums[i] == 1:
#                 for j in range(i + 1, len(nums)):
#                     if nums[j] == 0:
#                         result = max(result, j - i)
#                         break
#                 else:
#                     # 如果循环没遇到 0（即到结尾都是 1）
#                     result = max(result, len(nums) - i)
#         return result

# # 测试
# if __name__ == "__main__":
#     s = Solution()
#     print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))  # ✅ 输出: 3

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = cnt = 0
        for x in nums:
            if x:
                cnt += 1  # 连续 1 的个数增加
                ans = max(ans, cnt)  # 更新答案的最大值
            else:
                cnt = 0  # 重置
        return ans
# 测试
if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))  # ✅ 输出: 3
