#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        length = len(nums)
        if length <= k:
            return [max(nums)]
        queue = collections.deque([])
        res = []
        for i in range(length):
            if queue and queue[0] < i - k + 1:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res