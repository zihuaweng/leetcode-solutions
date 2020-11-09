#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# topological sorting
#
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        order = []

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            order.append(airport)

        dfs("JFK")
        return order[::-1]


# change to deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        order = collections.deque()

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            order.appendleft(airport)

        dfs("JFK")
        return order


class Topological:
    def topological_graph(self, vertices: list) -> list:  # vertices: [[a, b], [b,c]]
        # Build graph
        graph = collections.defaultdict(list)
        for a, b in vertices:
            graph[a].append(b)

        seen = set()
        stack = []

        for i in range(vertices):
            if i not in seen:
                self.dfs(graph, i, stack, seen)
        return stack[::-1]

    def dfs(self, graph, i, stack, seen):
        seen.add(i)
        for j in graph[i]:
            if j not in seen:
                self.dfs(graph, j, stack, seen)
        stack.append(i)
