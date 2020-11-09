#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 求最大公约数，最小公倍数
# https://blog.csdn.net/xiaoquantouer/article/details/61919470


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        def get_gcd(a, b):
            if b == 0:
                return a
            return get_gcd(b, a % b)

        l = len(points)
        if l == 0:
            return 0
        if l <= 2:
            return l
        res = 0
        for i in range(l - 1):
            d = collections.defaultdict(int)
            overlap = 0
            line_max = 0
            for j in range(i + 1, l):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if x == y == 0:
                    overlap += 1
                    continue
                gcd = get_gcd(x, y)      # 求公约数是因为如果直接用斜率作为key会遇到x/y, 分母为0的情况，会报错
                x /= gcd
                y /= gcd
                d[(x, y)] += 1
                line_max = max(line_max, d[(x, y)])
            res = max(res, line_max + overlap + 1)
        return res




