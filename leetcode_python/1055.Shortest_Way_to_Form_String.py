#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/shortest-way-to-form-string/
# dp


# Time complexity: O()
# Space complexity: O()


# 自己写的非常慢的解法
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        res = [0] + [float('inf')] * len(target)

        for i in range(1, len(res)):
            back_s = len(source) - 1
            back_t = i
            while back_t > 0 and back_s >= 0:
                if source[back_s] == target[back_t - 1]:
                    res[i] = min(res[i], res[back_t - 1] + 1)
                    back_t -= 1
                back_s -= 1
            if back_s < 0 and back_t == i:
                return -1

        return res[-1]


# two pointer
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        res = 0
        t = 0
        while t < len(target):
            check = t

            for s in source:
                if t < len(target) and s == target[t]:
                    t += 1

            if check == t:
                return -1
            res += 1

        return res


