#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        # find left bondary and right bondary
            1. left - > first on the left hand side that less than the current
            2. right -> first on right hand side that less than the current
            
            - > maintain an increasing stack
            
        # cal area:
            1. height: the last one in the stack [cause we find the right bondary]
            2. width: right - left -1 
            3. area = max(area, height * width)
            
        0  2  1.  5.  6.  2.  3  0
        0. 1.  2.  3.  4.  5  6. 7

        0. 1  5       2
        0. 2  3       5

        space:
        2 * (2-0-1) = 2
        6 * (5-3-1) = 6
        5 * (5-2-1) = 10
        """
        area = 0
        if not heights:
            return area
        stack = [-1]  # coner case. 解决stack最后一个的左边界问题
        heights.append(0)  # coner case。解决height最后一个右边界问题
        for idx, h in enumerate(heights):
            # 发现有比最后一个小的，计算面积
            while h < heights[stack[-1]]:
                cur_idx = stack.pop()
                right_idx = idx
                # 如果有相同的可以不用处理
                while heights[stack[-1]] == heights[cur_idx]:
                    stack.pop()
                left_idx = stack[-1]
                area = max(area, heights[cur_idx] * (right_idx - left_idx - 1))

            # 其余递增的则直接加入到stack里面
            stack.append(idx)

        return area
