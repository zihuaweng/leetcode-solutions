#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/minimum-cost-for-tickets/
# 经典dp问题

# Time complexity: O(n) n = 最后一天的长度
# Space complexity: O(n)

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 检索更快
        day_set = set(days)
        tickets = {a: b for a, b in zip([1, 7, 30], costs)}

        dp = [0] + [float('inf')] * days[-1]

        for i in range(1, len(dp)):
            if i in day_set:
                for k, l in tickets.items():
                    # 这里需要max(0, i - k)，因为车票有区间，可以整个覆盖，如果i<k，但是价格更低也是允许的
                    dp[i] = min(dp[max(0, i - k)] + l, dp[i])
            else:
                # 如果没有落入区间里面的证明不会超过之前计算的区间，可以直接等以前一个
                dp[i] = dp[i - 1]

        return dp[-1]


