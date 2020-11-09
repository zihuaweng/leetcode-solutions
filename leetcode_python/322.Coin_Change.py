#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/coin-change/
# 经典bottom-up， dp题目
# 子任务是 min(dp[i-coin_1], dp[i-coin_2], dp[i-coin_3) + 1

# Time complexity: O()
# Space complexity: O()

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
          0 1---------11  (amount)
        1  
        2 
        5 
        """
        dp = [0] + [amount + 1] * amount

        for i in range(1, len(dp)):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i - c] + 1, dp[i])

        if dp[-1] == amount + 1:
            return -1
        else:
            return dp[-1]
