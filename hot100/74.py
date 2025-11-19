from typing import List
from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]

# test
s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))  # Output: 5
