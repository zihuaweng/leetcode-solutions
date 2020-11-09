#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for edges, value in zip(equations, values):
            s, e = edges
            graph[s].append((e, value))
            graph[e].append((s, 1 / value))

        def calculate(query):
            s, e = query
            if s not in graph or e not in graph:
                return -1
            queue = collections.deque([(s, 1)])
            seen = set()
            while queue:
                node, cur_product = queue.popleft()
                if node == e:
                    return cur_product
                
                for next_node, value in graph[node]:
                    if next_node not in seen:
                        queue.append((next_node, value * cur_product))
                        seen.add(next_node)
            return -1

        return [calculate(query) for query in queries]



class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        a/b = 2         b/a = 1/2
        b/c = 3         c/b = 1/3
        
        a/c == a/b * b/c  6   (a -> b -> c)
        b/a == 1/2
        a/e e is not included, return -1 (corner case)
        a/a return 1 (corner case)
        
        graph
        dfs
        start: dd
        end: dd == d, or not matched value for d or dd
        """
        graph = collections.defaultdict(list)
        n = len(values)
        for i in range(n):
            dd, d = equations[i]
            graph[dd].append((d, values[i]))
            graph[d].append((dd, 1/values[i]))
            
        res = []
        for dd, d in queries:
            res.append(self.dfs(graph, dd, d, set()))
            
        return res
    
    def dfs(self, graph, dd, d, seen):
        if dd not in graph or d not in graph:
            return -1
        if dd == d:
            return 1
        
        seen.add(dd)
        
        for node, w in graph[dd]:
            if node in seen:
                continue
                
            res = self.dfs(graph, node, d, seen)
            if res != -1:
                return res * w
                
        return -1
            
            
        
            
            
            

