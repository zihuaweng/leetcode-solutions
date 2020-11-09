#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/maximal-rectangle/
# 具体参照 leetcode_python/84.Largest_Rectangle_in_Histogram.py

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        area = 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if i > 0 and matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

            area = max(area, self.largestRectangleArea(matrix[i]))
            # print(self.largestRectangleArea(matrix[i]))
        return area

    def largestRectangleArea(self, heights):
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