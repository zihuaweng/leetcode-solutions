#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 使用多个pointer完成

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        gap = float('inf')
        res = []
        heap = []
        gap_max = float('-inf')
        for i in range(len(nums)):
            gap_max = max(gap_max, nums[i][0])
            heapq.heappush(heap, (nums[i][0], 0, i))

        while heap:
            gap_min = heap[0][0]
            if gap_max - gap_min < gap:
                res = [gap_min, gap_max]
                gap = gap_max - gap_min
            _, i, idx = heapq.heappop(heap)
            if i == len(nums[idx]) - 1:
                break
            heapq.heappush(heap, (nums[idx][i + 1], i + 1, idx))
            gap_max = max(gap_max, nums[idx][i + 1])
        return res
