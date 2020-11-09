#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [x for x in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])      # path compression
            return parent[x]

        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            if p_x != p_y:
                parent[p_y] = p_x

        for u, v in edges:
            union(u, v)

        return len(set(find(x) for x in parent))   # 因为有的点并没有做到path compression，所以最后需要有一个find


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [x for x in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for x, y in edges:             # 这里只是简易化了上面，但是因为不能修改n, 所有吧union函数直击放在for loop下面。
            p_x = find(x)
            p_y = find(y)
            if p_x != p_y:
                parent[p_y] = p_x
                n -= 1

        return n
