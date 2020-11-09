#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf

# dp 解答：
# n^2
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        # print(dp)
        return max(dp)

# 一只生成新的数组，每次新数用二分搜索查找可以插入的位置，如果是==length就+1
# 否则就覆盖原来的数据
# nlogn
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp 的index代表长度为index+1 的递增序列最小的tail

        len = 1   :      [4], [5], [6], [3]   => dp[0] = 3
        len = 2   :      [4, 5], [5, 6]       => dp[1] = 5
        len = 3   :      [4, 5, 6]            => dp[2] = 6

        可以看出来一定是个递增的序列，所以我们可以用binary search来做。
        """ 
        dp = []
        for num in nums:
            idx = bisect.bisect_left(dp, num)
            # print(dp, idx)
            if idx == len(dp):
                dp.append(num)
            else:
                if dp[idx] > num:
                    dp[idx] = num

        return len(dp)



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * (n+1)
        dp[0] = float('-inf')
        size = 0
        for num in nums:
            l = 0
            r = n
            while l < r:
                m = (l+r) // 2
                if num > dp[m]:
                    l = m + 1
                else:
                    r = m
            
            index = l
            if dp[index-1] < num and num < dp[index]:
                dp[index] = num
                size = max(size, index)
        return size
