#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(A)
        n = len(A[0])
        # Get the first island
        stack = []
        found = False
        for i in range(m):
            if found:
                break
            for j in range(n):
                if A[i][j] == 1:
                    stack.append((i, j))
                    found = True
                    break
        # print(stack)

        # DFS get the boarder of first island
        border = []
        while stack:
            i, j = stack.pop()
            A[i][j] = -1

            for x, y in directs:
                if 0 <= x + i < m and 0 <= y + j < n:
                    if A[x + i][y + j] == 0:
                        border.append((i, j))
                    elif A[x + i][y + j] == 1:
                        stack.append((x + i, y + j))
        # print(border)
        # BFS gets the shortest path
        count = 0
        while border:
            new_b = []
            for i, j in border:
                for x, y in directs:
                    if 0 <= x + i < m and 0 <= y + j < n:
                        if A[x + i][y + j] == 1:
                            return count
                        elif A[x + i][y + j] == 0:
                            A[x + i][y + j] = -1
                            new_b.append((x + i, y + j))

            count += 1
            border = new_b


