<<<<<<< HEAD
import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

# 测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4], 2))  # 输出: 5
    print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # 输出: 4
=======
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
>>>>>>> fd1e44dbe4e0436644f97676d69a6dc25aa64916
