#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/walls-and-gates/
# 题目意思是从该点走几步到门（0的位置）

# Time complexity: O()
# Space complexity: O()


# 先从0开始，bsf辐散出去，每一步+1
# 利用了python的动态list
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if r == 0]
        for x, y in q:
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + i, y + j
                # 这里只需要判断inf (rooms[nx][ny] > 2 ** 30), 其他的结果要不数字更小（路径更短），不然就是墙（-1的位置）
                if 0 <= nx < len(rooms) and 0 <= ny < len(rooms[0]) and rooms[nx][ny] > 2 ** 30:
                    rooms[nx][ny] = rooms[x][y] + 1
                    q.append((nx, ny))


