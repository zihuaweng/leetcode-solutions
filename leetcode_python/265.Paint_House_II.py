#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(nk)
# Space complexity: O(1)

# https://leetcode.com/problems/paint-house-ii/

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        m = len(costs)
        n = len(costs[0])

        pre_min, pre_sec_min = 0, 0
        pre_min_idx = -1

        for i in range(m):
            cur_min, cur_sec_min = float('inf'), float('inf')
            cur_min_idx = 0
            for j in range(n):
                if j != pre_min_idx:
                    val = costs[i][j] + pre_min
                else:
                    val = costs[i][j] + pre_sec_min

                if val < cur_min:
                    cur_sec_min = cur_min
                    cur_min = val
                    cur_min_idx = j
                elif val < cur_sec_min:
                    cur_sec_min = val

            pre_min = cur_min
            pre_sec_min = cur_sec_min
            pre_min_idx = cur_min_idx

        return pre_min