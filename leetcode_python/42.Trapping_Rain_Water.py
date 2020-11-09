#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/trapping-rain-water/solution/

# 动态规划
# youtube.com/watch?v=wz00uI9mDXA
# 每个槽需要知道左边最高和右边最高，能承载的水量是当前的min(right_highest, left_highest[i]) - height[i]。
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        ans = 0

        left_highest = [0] * len(height)
        for i in range(1, len(left_highest)):
            left_highest[i] = max(left_highest[i - 1], height[i - 1])

        right_highest = 0
        for i in range(len(height) - 2, 0, -1):   # 第一个和最后一个不需要计算
            right_highest = max(right_highest, height[i+1])
            ans += max(min(right_highest, left_highest[i]) - height[i], 0)   # 需要max(res, 0), 因为蓄水不能为负数

        return ans


# 双指针方法
# https://leetcode.com/problems/trapping-rain-water/discuss/17391/Share-my-short-solution.


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0
        l = 0
        r = len(height) - 1
        res = 0
        while l <= r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            if left_max < right_max:
                res += left_max - height[l]
                l += 1
            else:
                res += right_max - height[r]
                r -= 1
        return res


# 维护单调递减的序列
# 和max Histogram那个题一样
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                cur = stack.pop()
                if stack:
                    res +=  (i-stack[-1]-1) * (min(h, height[stack[-1]]) - height[cur])
                
            stack.append(i)
        return res