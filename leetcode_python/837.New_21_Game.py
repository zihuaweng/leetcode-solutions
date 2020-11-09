#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/new-21-game/

# Time complexity: O(m)
# Space complexity: O()

# https://leetcode.com/problems/new-21-game/discuss/132503/My-take-on-how-to-reach-at-Solution

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        """
        x x x x x [i-w, i-w-1, i-w-2, ...., i-1] i
        prob(i) = sum([i-w, i-w-1, i-w-2, ...., i-1]) * 1/w
        
        expection:
        stop when we reach k
        so sum([i-w, i-w-1, i-w-2, ... i-1]) , we need to make sure:
            i-w >= 0
            i-1 < K
        this is O(W)
        
        time O(NW)
        
        optimization:
        we can use sliding window to calculate sum, each time, pre_sum - dp[i-w-1] + dp[i-1]
        this is O(1)
        x x x i-w-1 [i-w, i-w-1, i-w-2, ...., i-1] i
        
        time O(N)
        """
        dp = [0] * (N+1)
        dp[0] = 1

        pre_sum = 0
        for i in range(1, N+1):
            if i-W-1 >= 0:
                pre_sum -= dp[i-W-1]
            if i-1 < K:
                pre_sum += dp[i-1]
            
            dp[i] = pre_sum * 1/W
        # print(dp)
        return sum(dp[K:])


# 超时
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        d = {}
        return self.dfs(0, N, K, W, d)
    
    def dfs(self, cur, n, k, w, d):
        if cur in d:
            return d[cur]
        if cur >= k:
            if cur <= n:
                return 1
            else:
                return 0
            
        total = 0
        for i in range(1, w+1):
            total += 1/w * self.dfs(cur+i, n, k, w, d)
            
        d[cur] = total
        return total
        