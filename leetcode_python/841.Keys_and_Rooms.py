#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/keys-and-rooms/
# DFS

# Time complexity: O(N+K)
# Space complexity: O(N)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = collections.deque(rooms[0])
        opened = set()
        opened.add(0)
        while queue:
            cur = queue.pop()
            if cur not in opened:
                opened.add(cur)
                for i in rooms[cur]:
                    queue.append(i)

        return len(opened) == len(rooms)


# 模板
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        self.dfs(rooms, 0, seen)
        return len(seen) == len(rooms)

    def dfs(self, rooms, i, seen):
        seen.add(i)
        for j in rooms[i]:
            if j not in seen:
                self.dfs(rooms, j, seen)



