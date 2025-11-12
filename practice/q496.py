from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater ={}

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        while stack:
            next_greater[stack.pop()] = -1
        
        return [next_greater[x] for x in nums1]
# 测试
if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(solution.nextGreaterElement(nums1, nums2))  # 输出 [-1,3,-1]