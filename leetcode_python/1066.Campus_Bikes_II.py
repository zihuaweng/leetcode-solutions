#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/campus-bikes-ii/

# Time complexity: O()
# Space complexity: O()


class Solution:
    # 简单dfs需要n!计算， TLE
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n = len(bikes)
        visited = [False] * n
        return self.dfs(0, visited, workers, bikes)

    def dfs(self, i, visited, w, b):
        # print(i, visited)
        if i == len(w):
            return 0

        dist = float('inf')

        for j in range(len(visited)):
            if not visited[j]:
                visited[j] = True
                dist = min(dist, self.dfs(i + 1, visited, w, b) + self.dist(w[i], b[j]))
                visited[j] = False
                           
        return dist

    def dist(self, w, b):
        return abs(w[0] - b[0]) + abs(w[1] - b[1])


# 和上一个一样，但是使用了位运算保存state, dfs + momorization
# https://www.youtube.com/watch?v=nyOE2x5vTUk&t=640s
# 这里有具体的位运算解释
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n = len(bikes)
        mo = [0] * (1<<n)  
        return self.dfs(0, mo, 0, workers, bikes)

    def dfs(self, i, mo, state, w, b):
        # print(i, visited)
        if i == len(w):
            return 0
        if mo[state] != 0:
            return mo[state]

        dist = float('inf')

        for j in range(len(b)):
            if state & (1<<j) == 0:
                st = state | (1<<j)
                dist = min(dist, self.dfs(i + 1, mo, st, w, b) + self.dist(w[i], b[j]))
                    
        mo[state] = dist
        return dist

    def dist(self, w, b):
        return abs(w[0] - b[0]) + abs(w[1] - b[1])

# 使用 priorityqueue , 类似Djikstra's
# https://leetcode.com/problems/campus-bikes-ii/discuss/303422/Python-Priority-Queue
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        def dist(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])

        h = [[0, 0, 0]]
        seen = set()
        while True:
            cost, i, token = heapq.heappop(h)
            if (i, token) not in seen:
                seen.add((i, token))
                if i == len(workers):
                    return cost
                for j in range(len(bikes)):
                    if token & (1 << j) == 0:
                        heapq.heappush(h, [cost + dist(i, j), i + 1, token | (1 << j)])

