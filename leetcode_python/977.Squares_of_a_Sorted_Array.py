#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(map(lambda x: x*x, A))


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        l = 0
        r = len(A) - 1
        while l <= r:
            if abs(A[l]) > abs(A[r]):
                res.append(A[l] ** 2)
                l += 1
            else:
                res.append(A[r] ** 2)
                r -= 1

        return res[::-1]
