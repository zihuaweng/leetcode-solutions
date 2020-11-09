#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/minimum-knight-moves/

# 另一种方法
# https://leetcode.com/problems/minimum-knight-moves/discuss/387120/Python3-Clear-short-and-easy-DP-solution-No-Need-for-BFS-or-math

# 暴力bfs，因为走棋盘是对称的，所以我们可以只看正整数的一遍
# 判断new_x > -4 and new_y > -4可以忽略负数区域，就可以解决Time Limit Exceeded问题
# new_x > -2 and new_y > -2 也能通过

class Solution:
    def minKnightMoves(self, t_x: int, t_y: int) -> int:
        t_x, t_y = abs(t_x), abs(t_y)
        if t_x == 0 and t_y == 0:
            return 0
        direction = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        queue = [(0, 0)]
        visited = set()
        depth = 0
        while queue:
            temp = []
            depth += 1
            for q in queue:
                x, y = q
                for _x, _y in direction:
                    new_x = x + _x
                    new_y = y + _y

                    if (new_x, new_y) not in visited and new_x > -4 and new_y > -4:
                        if new_x == t_x and new_y == t_y:
                            return depth
                        visited.add((new_x, new_y))
                        temp.append((new_x, new_y))
            queue = temp


