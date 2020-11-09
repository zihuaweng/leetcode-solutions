#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = collections.Counter(nums)
        end = collections.Counter()
        for n in nums:
            if left[n]:
                left[n] -= 1
                if end[n - 1] > 0:
                    end[n - 1] -= 1
                    end[n] += 1
                elif left[n + 1] and left[n + 2]:
                    left[n + 1] -= 1
                    left[n + 2] -= 1
                    end[n + 2] += 1
                else:
                    return False

        return True