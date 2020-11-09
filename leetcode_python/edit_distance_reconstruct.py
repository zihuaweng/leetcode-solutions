class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m+1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j - 1]+ 1, dp[i-1][j-1]+(word1[i - 1] != word2[j - 1]))

        print(self.construct(dp, word1, word2))
        print(dp)
        return dp[-1][-1]

    def construct(self, dp, word1, word2):
        i = len(dp)-1
        j = len(dp[0])-1
        
        path = []
        while i > 0 and j>0:
            if word1[i-1] == word2[j-1]:
                path.append(word1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j-1] < dp[i][j-1] and dp[i-1][j-1] < dp[i-1][j]:
                path.append('replace ' + word1[i-1] + ' to ' + word2[j-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] < dp[i][j-1]:
                path.append('-' + word1[i-1])
                i -= 1
            else:
                path.append('+' + word2[j-1])
                j -= 1

        return path[::-1]


print(Solution().minDistance("AABACC", "BABCAC"))

[[0, 1, 2, 3, 4, 5, 6], 
[1, 1, 1, 2, 3, 4, 5],
[2, 2, 1, 2, 3, 3, 4], 
[3, 2, 2, 1, 2, 3, 4], 
[4, 3, 2, 2, 2, 2, 3], 
[5, 4, 3, 3, 2, 3, 2], 
[6, 5, 4, 4, 3, 3, 3]]