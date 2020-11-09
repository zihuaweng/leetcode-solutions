#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

# Time complexity: O()
# Space complexity: O()

# 观察，因为只能上下交换，所以可以出现的相同的数，不是A[0]就是B[0]，否则就返回-1


class Solution:
    # 如果可以得到解的话，说明 A中目标的个数+ B目标个数 - AB同一位置出现相同的个数 == N
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        for i in range(1, 7):
            if all(i in p for p in zip(A, B)):
                return n - max(A.count(i), B.count(i))
        return -1

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)

        # 检查AB能否换成A[0], ab记录更换次数
        i = 0
        a = b = 0
        # a -> B to A
        # b -> A to B
        while i < n and (A[i] == A[0] or B[i] == A[0]):
            if A[i] != A[0]: a += 1
            if B[i] != A[0]: b += 1
            if i == n - 1: return min(a, b)
            i += 1

        # 检查AB能否换成B[0], ab记录更换次数
        i = 0
        a = b = 0
        # a -> B to A
        # b -> A to B
        while i < n and (A[i] == B[0] or B[i] == B[0]):
            if A[i] != B[0]: a += 1
            if B[i] != B[0]: b += 1
            if i == n - 1: return min(a, b)
            i += 1

        return -1
