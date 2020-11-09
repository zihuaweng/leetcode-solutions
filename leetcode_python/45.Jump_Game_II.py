#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# [2,3,1,1,4]
# [0,1,2,3,4]
# 开始 0
# 第一步 1,2 走到2为当前终点，需要走第二步
# 第二部 3,4，到4就到达终点了
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        max_end = 0
        step = 0
        for i, val in enumerate(nums[:-1]):
            max_end = max(max_end, i + val)
            if i == end:
                end = max_end
                step += 1
        return step


# 与55 类似的代码
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        start = end = 0
        step = 0
        if n == 1:
            return step
        
        while start <= end:
            new_end = 0
            for i in range(start, end+1):
                new_end = max(new_end, i+nums[i])
                if new_end >= n-1:
                    return step + 1
            step += 1
            start = end + 1
            end = new_end
            
        return -1

