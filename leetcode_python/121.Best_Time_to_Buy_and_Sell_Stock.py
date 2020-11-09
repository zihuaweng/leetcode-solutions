# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            [7,1,5,3,6,4]
        1. buy at the lowest point:  get min() of prev nums
        2. sell it at highest point, any point could be the sell point: cal profit for each point (sell point)
        """
        if not prices:
            return 0
        
        buy = float('inf')
        profit = float('-inf')
        for p in prices:
            if p < buy:
                buy = p
            
            profit = max(profit, p-buy)
            
        return profit
            
        