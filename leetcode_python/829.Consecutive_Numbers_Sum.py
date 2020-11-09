#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/consecutive-numbers-sum/
# https://leetcode.com/problems/consecutive-numbers-sum/discuss/129015/5-lines-C%2B%2B-solution-with-detailed-mathematical-explanation.

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 1
        for i in range(2, int(N**0.5+1)):
            if (N-(i*i + i)/2) % i == 0:
                count += 1
        return count