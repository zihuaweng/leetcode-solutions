#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# https://leetcode.com/problems/grumpy-bookstore-owner/


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        exist_sum = 0
        pre_sum = 0
        extra = 0
        for i in range(len(customers)):
            c = customers[i]
            g = grumpy[i]
            if g == 0:
                exist_sum += c
            if i >= X:
                pre_sum -= customers[i - X] * grumpy[i - X]
            pre_sum += c * g
            extra = max(extra, pre_sum)

        return exist_sum + extra

