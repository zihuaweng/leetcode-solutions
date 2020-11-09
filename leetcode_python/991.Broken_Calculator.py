#!/usr/bin/env python3
# coding: utf-8


# https://buptwc.com/2019/02/10/Leetcode-991-Broken-Calculator/

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if Y < X:
            return X-Y
        res = 0
        while X < Y:
            if Y % 2 == 1:
                Y += 1
                res += 1
            Y //= 2
            res += 1
        return res + X - Y