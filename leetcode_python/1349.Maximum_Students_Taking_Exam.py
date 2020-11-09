#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(2**n * 2**n) = O(2**2n)
# Space complexity: O(2**n)


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0])
        valid_seats = [0] * m
        for i in range(m):
            for j in range(n):
                valid_seats[i] |= 1 << j if seats[i][j] == '.' else 0

        def count_bit(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1

            return count

        dp = [-1] * (1 << n)
        for i in range(m):
            temp = [-1] * (1 << n)
            for j in range(valid_seats[i] + 1):  # 这里也可以是 range(1<<n)， 因为最多是valid_seats[i]个所以不用遍历所有1<<n
                if j & valid_seats[i] == j and j & (j >> 1) == 0:  # 判断是否是一个子集，证明没有broken seat，然后判断有没有相邻的位置被占了
                    if i == 0:
                        temp[j] = count_bit(j)  # 填第一行
                    else:
                        for k in range(1 << n):  # k代表上一轮能走到的state， 我们从上一轮的所有state，state j能到的数
                            if k & (j >> 1) == 0 and (k >> 1) & j == 0 and dp[k] != -1:  # 看右上角，左上角有没有被占了，然后看k这个state上一轮能不能走到
                                temp[j] = max(temp[j], dp[k] + count_bit(j))
            dp = temp

        return max(dp)

# same idea
from functools import lru_cache


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0])
        valid_seats = [0] * m
        for i in range(m):
            for j in range(n):
                valid_seats[i] |= 1 << j if seats[i][j] == '.' else 0

        def count_bit(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1

            return count

        @lru_cache(None)
        def func(pre_state, row):
            if row == m:
                return 0
            res = 0
            for state in range(valid_seats[row] + 1):
                if state & valid_seats[row] == state and state & (state >> 1) == 0:
                    if pre_state & (state >> 1) == 0 and (pre_state >> 1) & state == 0:
                        res = max(res, count_bit(state) + func(state, row + 1))
            return res

        return func(0, 0)