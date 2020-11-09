#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/146579/Easy-python-28-ms-beats-99.5
# 比较难，需要递归dfs完成。

# Time complexity: O(k*2^n)
# Space complexity: O()


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        nums = [4, 3, 2, 3, 5, 2, 1], k = 4

        target = sum(nums) // k

        - sum(nums) % k !== 0

        [4, 3, 2, 3, 5, 2, 1]         
        0   0
        1   1
        2   2
        3   3

        - for each group, when we put a num, the group_sum <= target, otherwise, put the num to the next group   
            dfs, recursive, 
            group_sum = [0] * k
        - if a num if not able to be put in a group where group_sum <= target, fail to split nums into k groups
        - when we reach to the end of nums, we return true

        time O(n^k)
        For each item, try all possible destined bucket
        space O()

        """
        if not nums or len(nums) < k:
            return False
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)  # 倒排更快
        set_sum = [0] * k
        average_sum = sum(nums) // k

        def dfs(index):
            if index == len(nums):
                return True
            for i in range(k):
                set_sum[i] += nums[index]
                if set_sum[i] <= average_sum and dfs(index + 1):
                    return True
                set_sum[i] -= nums[index]
                if set_sum[i] == 0:  # 如果这个数不符合条件就没必要尝试别的空篮子，速度提高很多
                    break
            return False

        return dfs(0)