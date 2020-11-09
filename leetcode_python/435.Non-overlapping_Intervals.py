#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/non-overlapping-intervals/
# 这个题目和书本明星排档期一样，需要选择最多不重叠的区间，最好的方法是看最快结束的段
# 如果后面起始点有小于这个结束时间的删除。

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        end = float('-inf')
        res = 0
        for i in intervals:
            if i[0] < end:
                res += 1
            else:
                end = i[1]
        return res
