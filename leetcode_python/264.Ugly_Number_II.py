#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/ugly-number-ii/

# drawing note in OneNote
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            res = min([u2, u3, u5])
            if res == u2:
                i2 += 1
            if res == u3:
                i3 += 1
            if res == u5:
                i5 += 1
            ugly.append(res)

        # print(ugly)
        # print(i2,i3,i5)

        return ugly[-1]


## this is kind of nlog(h) solution
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [2, 3, 5]
        res = [1]
        while len(res) < n:
            next_n = heapq.heappop(heap)
            while next_n == res[-1]:
                next_n = heapq.heappop(heap)
            res.append(next_n)
            for i in [2, 3, 5]:
                heapq.heappush(heap, next_n * i)

        return res[-1]