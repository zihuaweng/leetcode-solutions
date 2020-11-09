#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return True

        gap = A[1] - A[0]
        for i in range(2, len(A)):
            temp = A[i] - A[i - 1]
            if temp * gap < 0:
                return False
            if temp != 0:
                gap = temp

        return True


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increase = False
        decrease = False

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                increase = True
            if A[i] < A[i - 1]:
                decrease = True

        return not (decrease and increase)