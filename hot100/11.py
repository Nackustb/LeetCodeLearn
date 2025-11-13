# from collections import deque
# from typing import List
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         q = deque()  
#         res = []
#         for i, num in enumerate(nums):
#             while q and nums[q[-1]] < num:
#                 q.pop()
#             q.append(i)

#             if q[0] <= i - k:
#                 q.popleft()

#             if i >= k - 1:
#                 res.append(nums[q[0]])
#         return res
    
# # Example usage:
# sol = Solution()
# print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [3,3,5,5,6,7]

from typing import List
from heapq import heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        for i in range(len(nums)):
            heappush(max_heap, (-nums[i], i))

            if i >= k - 1:
                while max_heap[0][1] <= i - k:
                    heappop(max_heap)
                res.append(-max_heap[0][0])
        return res