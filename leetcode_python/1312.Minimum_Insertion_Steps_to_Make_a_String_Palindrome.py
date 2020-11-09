class Solution:
    def minInsertions(self, s: str) -> int:
        """
        i [x] xxxx [x]  j
          i+1      j-1
        
        dp[i][j] : the minimum number of steps to make s[i:j+1] palindrome.
        
        
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1]
        else:
            add one before i that equals to j
                j i xxxxx j
            or
            add one after j that equals to i
                i xxxxx j i
                
            dp[i][j] = min(dp[i][j-1], dp[i+1][j]) + 1
        
        """
        n = len(s)
        
        dp = [[0] * n for _ in range(n)]
        
        for l in range(2, n+1):
            for i in range(n-l+1):  # in case j is out of index
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i+1][j]) + 1

        return dp[0][n-1]