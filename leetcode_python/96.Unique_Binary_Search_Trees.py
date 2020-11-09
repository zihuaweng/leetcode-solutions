# https://leetcode.com/problems/unique-binary-search-trees/
# https://www.cnblogs.com/grandyang/p/4299608.html
# 需要会看

class Solution:
    def numTrees(self, n: int) -> int:
        # write your code here
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n - 2)]
            for i in range(3, n + 1):  # 这里是循环计算每个n对应的树，只有计算了前面的才能计算后面的n
                for j in range(0, i):  # 这里是计算当n为特定值的时候的树。 n=3，则需要知道n=0,1,2时的树数量
                    dp[i] += dp[j] * dp[i - j - 1]
            return dp[n]
