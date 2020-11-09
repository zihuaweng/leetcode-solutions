#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/friend-circles/
# 这个题目是需要将方阵的长度个人分成不同群体，可以使用dfs

# Time complexity: O(N+K)
# Space complexity: O(N)

# 与200题一样模板
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        if not M:
            return 0

        seen = set()
        m = len(M)
        for i in range(m):
            if i not in seen:
                count += 1
                self.dfs(M, seen, i)
        return count

    def dfs(self, M, seen, i):
        seen.add(i)
        for idx, num in enumerate(M[i]):
            if num == 1 and idx not in seen:
                self.dfs(M, seen, idx)


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        seen = set()

        def dfs(node):
            for i, j in enumerate(M[node]):
                if j == 1 and i not in seen:
                    seen.add(i)
                    dfs(i)

        res = 0
        for i in range(len(M)):
            if i not in seen:
                dfs(i)
                res += 1

        return res

# union find
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        parent = {i: i for i in range(n)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            if p_x != p_y:
                parent[p_y] = p_x

        for i in range(n-1):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    union(i, j)

        for i in range(n):
            find(i)

        return len(set(parent.values()))
