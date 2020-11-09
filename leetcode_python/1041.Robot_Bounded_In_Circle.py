#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/robot-bounded-in-circle/

# 只要能够回到原点，或者方向不是朝上的，就会有回路
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dx = 0
        dy = 1
        for i in instructions:
            if i == 'R':
                dx, dy = dy, -dx
            if i == 'L':
                dx, dy = -dy, dx
            if i == 'G':
                x += dx
                y += dy
        return (x,y) == (0,0) or (dx,dy) != (0,1)