#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/subarray-sum-equals-k/

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pre_sum = 0
        counter = collections.Counter()
        counter[0] = 1
        for num in nums:
            pre_sum += num
            target = pre_sum - k
            res += counter[target]
            counter[pre_sum] += 1
        return res
