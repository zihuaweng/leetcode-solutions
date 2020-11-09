#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/partition-equal-subset-sum/
# 同698，答案还需要琢磨

# Time complexity: O()
# Space complexity: O()

# no good
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        average_sum = sum(nums) // 2

        # nums.sort(reverse=True)

        def dfs(index, target):
            if target == 0:
                return True
            if index >= len(nums) or target < 0:
                return False
            if dfs(index + 1, target - nums[index]):
                return True
            j = index + 1
            while j < len(nums) and nums[j] == nums[index]:
                j += 1
            return dfs(j, target)

        return dfs(0, average_sum)



# optimal solution, dp, knapsack question
# time O(sum*n)
class Solution2:
    def canPartition(self, nums: List[int]) -> bool:

        # dp[j] 表示从 0-average_sum， 有没有组合可以到达这个位置

        if sum(nums) % 2:
            return False
        average_sum = sum(nums) // 2

        dp = [False] * (average_sum + 1)
        dp[0] = True
        for n in nums:
            for j in range(average_sum, -1, -1):
                if j >= n:
                    dp[j] = dp[j] or dp[j - n]
        return dp[-1]
