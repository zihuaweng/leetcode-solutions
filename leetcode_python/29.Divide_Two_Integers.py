#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig = (dividend < 0) == (divisor < 0)
        a, b, res = abs(dividend), abs(divisor), 0
        while a >= b:
            shift = 0
            while a >= b << (shift+1):
                print(a, res)
                shift += 1
            res += 1 << shift
            a -= b << shift
        return min(res if sig else -res, (1<<31)-1)


a = Solution()
print(a.divide(-1<<31,0))