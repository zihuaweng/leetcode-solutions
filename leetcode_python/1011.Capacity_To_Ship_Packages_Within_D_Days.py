#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 410一样的代码

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        
        while lo < hi:
            mid = (lo+hi) // 2
            days = self.get_days(weights, mid)
            if days > D:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    def get_days(self, weights, target):
        days = 0
        cur_w = 0
        for w in weights:
            if cur_w + w > target:
                days += 1
                cur_w = w
            else:
                cur_w += w
        days += 1
        return days