from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]


# class Solution(object):
#     def twoSum(self, nums, target):
#         # 遍历列表
#         for i in range(len(nums)):
#             res = target-nums[i]
#             if res in nums[i+1:]:
#                 return [i, nums[i+1:].index(res)+i+1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for index, num in enumerate(nums):
            if target - num in hashtable:
                return[hashtable[target - num],index]
            else:
                hashtable[num] = index
        return []

# # 测试
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # 输出: [0, 1]