from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float('+inf'), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
    
# test
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))  # 5
