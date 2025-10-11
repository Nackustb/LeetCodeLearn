from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
# test
s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))  # 5