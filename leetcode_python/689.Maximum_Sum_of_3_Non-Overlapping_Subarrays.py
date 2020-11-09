#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://www.youtube.com/watch?v=dGS4O0110qA
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
# 太难没搞懂


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)

        w1 = sum(nums[:k])
        w2 = sum(nums[k:k * 2])
        w3 = sum(nums[k * 2:k * 3])

        mw1, mw2, mw3 = w1, w1 + w2, w1 + w2 + w3
        mw1index, mw2index, mw3index = [0], [0, k], [0, k, 2 * k]  # mw1,mw2,mw3's index.
        for i in range(1, n - 3 * k + 1):  # last index for w1 window will be n-3k
            w1 += nums[i - 1 + k] - nums[i - 1]
            w2 += nums[i - 1 + 2 * k] - nums[i - 1 + k]
            w3 += nums[i - 1 + 3 * k] - nums[i - 1 + 2 * k]
            if w1 > mw1:
                mw1, mw1index = w1, [i]
            if mw1 + w2 > mw2:
                mw2, mw2index = mw1 + w2, mw1index + [i + k]
            if mw2 + w3 > mw3:
                mw3, mw3index = mw2 + w3, mw2index + [i + 2 * k]
        return mw3index
