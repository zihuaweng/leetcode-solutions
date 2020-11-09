#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:

        #         n * n <= x < (n+1) * (n+1)
        #         x / n >= n
        #         x / (n+1) < (n+1)

        #         1 2 3 4 5 6 7 8
        #         i     mid        j
        #         i . j

        #         1 2 3 4

        i = 1
        j = x
        ans = 0

        while i <= j:
            mid = (i + j) // 2
            if x / mid < mid:
                j = mid - 1
            else:
                # // upper
                # bound的形式，因为我们要找的ans要是最接近于x的最大的数，利用upper
                # bound
                i = mid + 1
                ans = mid

        return ans

# 最后return r有点类似左右边界的问题，但是这里是如果有整数结果，就在中间返回，
# 否则就返回r,即向上取整的结果
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        while l <= r:
            # print(l,r)
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1

        return r




