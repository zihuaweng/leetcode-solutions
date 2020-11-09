#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# https://www.jianshu.com/p/30d2058db7f7


# Time complexity: O()
# Space complexity: O()

class Solution:
    def removeStones(self, points):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        for i, j in points:
            rows[i].add(j)
            cols[j].add(i)

        def dfsRow(i):
            seenR.add(i)
            for j in rows[i]:
                if j not in seenC:
                    dfsCol(j)

        def dfsCol(j):
            seenC.add(j)
            for i in cols[j]:
                if i not in seenR:
                    dfsRow(i)

        seenR, seenC = set(), set()
        islands = 0
        for i, j in points:
            if i not in seenR:
                islands += 1
                dfsRow(i)
                dfsCol(j)
        return len(points) - islands

# union find 做法
class Solution:
    def removeStones(self, points):
        uf = {}

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            uf[find(x)] = find(y)

        for x, y in points:
            union(x, ~y)  #使用～是用来区别x,y

        return len(points) - len(set(find(x) for x in uf))