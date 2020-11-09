#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/gas-station/
# 比较难理解

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_sum = 0
        cur_sum = 0
        s = 0
        for i in range(len(gas)):
            total_sum += gas[i] - cost[i]  # 用来计算所有路程的总油量与消耗比较，总油量<消耗，就不会有解
            cur_sum += gas[i] - cost[i]  # 计算当前位置能否走到下一个位置，当前油量需要大于消耗量
            if cur_sum < 0:
                s = i + 1
                cur_sum = 0

        if total_sum >= 0:
            return s
        else:
            return -1