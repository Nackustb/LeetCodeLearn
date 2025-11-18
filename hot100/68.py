from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2  # 合并列表
        nums.sort()           # 排序
        n = len(nums)
        mid = n // 2
        if n % 2 == 1:        # 奇数长度，返回中间值
            return nums[mid]
        else:                 # 偶数长度，返回中间两个数平均值
            return (nums[mid - 1] + nums[mid]) / 2
        