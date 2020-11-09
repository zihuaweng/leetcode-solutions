
# https://leetcode.com/problems/ones-and-zeroes/


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        one of the knapsack questions. 
        current value depends on if we count current value or not.

        dp[i][j] == number of string we can have with i 0 and j 1.
        """
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for s in strs:
            ones = zeros = 0
            for char in s:
                ones += char == '1'
                zeros += char == '0'
                
            for i in range(m, zeros-1, -1):       # we need to update the value from right bottom corner case we update current value using the previous value.
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
        return dp[-1][-1]