#!/usr/bin/env python3
# coding: utf-8

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        _sum = sum([i for i, j in costs])
        diff = [j-i for i, j in costs]
        return _sum + sum(sorted(diff)[:len(costs) // 2])