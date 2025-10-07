from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
                
        
        return [next_greater.get(x, -1) for x in nums1]        
    
# 测试
if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(solution.nextGreaterElement(nums1, nums2))  # 输出 [-1,3,-1]