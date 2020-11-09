#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = []
        res = 0
        for val in nums:
            idx = bisect.bisect_left(dp, val)
            if idx == res:
                dp.append(val)
                res += 1
                if res == 3:
                    return True
            else:
                dp[idx] = val

        return False


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for val in nums:
            if val <= first:
                first = val
            elif val <= second:
                second = val
            else:
                return True

        return False
