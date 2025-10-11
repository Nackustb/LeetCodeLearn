from heapq import heappop, heappush
from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for word, freq in count.items():
            heappush(heap, (-freq, word))

        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])    
        return res
    
# test
s = Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))  # ["i", "love"]
