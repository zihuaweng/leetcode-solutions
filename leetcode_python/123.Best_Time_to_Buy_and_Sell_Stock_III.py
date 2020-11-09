# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        we could have 4 states.
        1. can only hold one stock at a time
        2. need to sell before next buy
        
        hold1 -> sold1 -> hold2 -> sold2
        
        on the kth day:
            each state: we can do the transaction , or not do the transaction
        
        hold1[k] = max(hold1[k-1], -p)
        sold1[k] = max(sold1[k-1], hold1[k-1]+p)
        hold2[k] = max(hold2[k-1], sold1[k-1]-p)
        sold2[k] = max(sold2[k-1], hold2[k-1]+p)
        
        result = max(sold1, sold2)
        """
        hold1 = float('-inf')        
        sold1 = 0
        hold2 = float('-inf')        
        sold2 = 0
        
        for p in prices:
            hold1_temp = hold1   
            sold1_temp = sold1
            hold2_temp = hold2
            sold2_temp = sold2
            
            hold1 = max(hold1_temp, -p)
            sold1 = max(sold1_temp, hold1_temp+p)
            hold2 = max(hold2_temp, sold1_temp-p)
            sold2 = max(sold2_temp, hold2_temp+p)
            
        return max(sold1, sold2)