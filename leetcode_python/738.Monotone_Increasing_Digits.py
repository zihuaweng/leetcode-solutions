#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/monotone-increasing-digits/

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        n = [int(i) for i in str(N)]
        j = -1
        for i in range(len(n)-1, 0, -1):
            if n[i] < n[i-1]:
                j = i
                n[i-1] -= 1
        if j == -1:
            return N
        while j < len(n):
            n[j] = 9
            j+=1
        return int(''.join([str(i) for i in n]))