#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 超时
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        return self.helper(amount, 0, 0, coins)

    def helper(self, amount, idx, temp, coins):
        if temp == amount:
            return 1
        res = 0
        for i in range(idx, len(coins)):
            if temp + coins[i] > amount:
                break
            res += self.helper(amount, i, temp + coins[i], coins)
        return res


# O(amount * n)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(1, amount + 1):
                if i - c >= 0:
                    dp[i] += dp[i - c]
        return dp[-1]
