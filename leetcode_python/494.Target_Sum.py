#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        seen = {}
        return self.dfs(nums, S, 0, 0, seen)

    def dfs(self, nums, target, temp, idx, seen):

        if (idx, temp) in seen:
            return seen[(idx, temp)]

        if idx == len(nums):
            if temp == target:
                return 1
            else:
                return 0

        add = self.dfs(nums, target, temp - nums[idx], idx + 1, seen)
        minus = self.dfs(nums, target, temp + nums[idx], idx + 1, seen)
        seen[(idx, temp)] = add + minus
        return add + minus


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        #         1 2 2    3

        #         -5  -4  -3  -2  -1  0  1  2  3  4  5
        #    0                        1
        #    1                     1     1
        #    2             1       1     1     1
        #    3     1       1       2     2     1     1

        if not nums:
            return 0

        total_sum = sum(nums)
        if total_sum < S or -total_sum > S:
            return 0
        n = len(nums)
        dp = [[0] * (2 * total_sum + 1) for _ in range(n + 1)]
        dp[0][total_sum] = 1
        for i in range(1, n + 1):
            for j in range(2 * total_sum + 1):
                if dp[i - 1][j] != 0:
                    dp[i][j - nums[i - 1]] += dp[i - 1][j]
                    dp[i][j + nums[i - 1]] += dp[i - 1][j]
        # print(dp)

        return dp[n][total_sum + S]





