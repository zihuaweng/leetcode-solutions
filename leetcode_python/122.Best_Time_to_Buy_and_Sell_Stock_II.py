# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
           4
          3        9
         2       7
        1     2
        
        so 4 is highest， 1 is the lowest. cur profit is 4-1 = 3
        so 9 is highest， 2 is the lowest. cur profit is 9-2 = 7
        total = 10
        
        we don't need to get the highest, just add the diff of adjacent num
        
        time O(n)
        """
        profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
                
        return profit
        