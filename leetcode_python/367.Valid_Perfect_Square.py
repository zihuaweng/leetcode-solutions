#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/valid-perfect-square/discuss/130010/Python-4-Methods-with-time-testing

# log(n) < sqrt(n)

# sqrt(n)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        while i*i <= num:
            if i*i == num:
                return True
            i += 1
        return False

# log(n)
    def BinarySearch(self, num):
        left = 0
        right = num

        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False