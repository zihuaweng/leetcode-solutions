#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for n in range(1, num + 1):
            if n & 1 == 0:
                dp[n] = dp[n >> 1]
            else:
                dp[n] = dp[n - 1] + 1
        return dp
