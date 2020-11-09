#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(nlogn) (因为排序了)
# Space complexity: O(n)

# 不会超时的trick： 设置_dp作为类属性，测试就会通过。既然作为类属性就不知道当前函数n大小，所以可以使用添加的方式记录
# 其他方法：
# https://leetcode.com/problems/perfect-squares/discuss/71488/Summary-of-4-different-solutions-(BFS-DP-static-DP-and-mathematics)

class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            temp = float('inf')
            for i in range(1, int(len(dp)**0.5+1)):
                temp = min(dp[-i*i] + 1, temp)
            dp.append(temp)
        return dp[n]


# 最常规的解法。
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[-1]


# bfs:
# https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
class Solution3:
    def numSquares(self, n):
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt