class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        red  blue  green
        17    2     17
        18    33    7
        
        1. cur color cost = cur + min(other color)
        """
        if not costs:
            return 0
        
        dp = costs[0]
        
        for r, b, g in costs[1:]:
            temp = [0] * 3
            temp[0] = r+min([dp[1], dp[2]])
            temp[1] = b+min([dp[0], dp[2]])
            temp[2] = g+min([dp[0], dp[1]])
            dp = temp
            
        return min(dp)